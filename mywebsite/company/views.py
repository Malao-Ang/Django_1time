from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from songline import Sendline #ส่งไลน์
from .emailsystem import sendthai #ส่งเมล
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import uuid
from django.core.files.storage import FileSystemStorage
def Login(request):
    context = {}#สิ่งที่จะใส่เข้าไป

    if request.method == 'POST': #if กดปุ่มเข้ามา
        data = request.POST.copy()
        username = data.get('username')
        password = data.get('password')

        try:
            user = authenticate(username=username, password=password)
            login(request,user)  
            return redirect('home-page')
        except:    
            context['massage'] = 'username or password not correct please try again'
    return render(request, 'company/login.html',context)
# def Home(request):
#     return HttpResponse('<h1>Hello World!<h1> <br> <p>by Kaewmanee</p>')

def Home(request):
    allproduct = Product.objects.all() # SELECT * fome product
    context = {'allproduct':allproduct}
    return render(request, 'company/home.html',context) #company ที่อยู่ใน template

def Aboutus(request):
    return render(request, 'company/aboutus.html')

def ContactUs(request):

    context = {}#สิ่งที่จะใส่เข้าไป

    if request.method == 'POST': #if กดปุ่มเข้ามา
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')
        print(title)
        print(email)
        print(detail)
        print('---------------')

        #กรณีกรอกข้อมูลไม่ครบ
        if title == '' and email == '':
            context['massage'] = 'โปรดใส่ title และ email ให้เรียบร้อย เพื่อความสะดวกในการติดต่อ' 
            return render(request, 'company/contact.html',context)


        #ได้ข้อมูลแล้วทำการบันทึกข้อมูล
        newrecord = ContactList()
        newrecord.title = title
        newrecord.email = email
        newrecord.detail = detail
        newrecord.save()
        context['massage'] = "ข้อความได้ส่งไปเรียบร้อยแล้วกรุณารอการตอบกลับภายใน 24 ชั่วโมง"
        token = 'XLsgUQxFATU9TTHADBlxgAXUMX2SZU92QcYcQ4ayBis'

        #แจ้งemail กลับ
        text =  'สวัสดีคุณลูกค้าที่เคารพ\n\nทางรับได้รับemailเรียบร้อยแล้วเราจะตอบกลับท่านให้เร็วที่สุด\n\nท่านสามารถติดต่อทางช่องทางอื่นได้อีก :\n\nLineID : 0813064437\n\nfacebook : w.computer'
        sendthai(email,'W.computer :สอบถามปัญหา',text)

            # token สามารถสมัคร+ยกเลิกได้ผ่านทาง line notify

        m = Sendline(token)
        m.sendtext('\ntitle:{} \nemail:{} \n>>>{}'.format(title,email,detail))
        #บันทึกข้อมูล
        #ทำให้เหลือบรรทัดเดียว
        #ContactList(title=newrecord.title, email=newrecord.email).save()

    return render(request, 'company/contact.html',context)

@login_required
def Accountant(request):
    allow_user = ['accountant','admin']
    if request.user.profile.usertype not in allow_user: 
        return redirect('home-page')
    contact = ContactList.objects.all() # ดึง ContactListมาใช้
    context = {'contact':contact}
    return render(request, 'company/accountant.html',context)

def Register(request):
    context = {}#สิ่งที่จะใส่เข้าไป

    if request.method == 'POST': #if กดปุ่มเข้ามา

        data = request.POST.copy()
        fullname = data.get('fullname')
        email = data.get('email')
        mobile = data.get('mobile')
        password = data.get('password')
        password2 = data.get('password2')

        username = email

        try :
            check = User.objects.get(username = username )
            context['warning'] =f'This email ({ username }) has already been used.'
            return render(request, 'company/register.html',context)
            return redirect('home-page')

        except:
            if password != password2:
                context['warning'] ='Password not Correct please try again.'
                return render(request, 'company/register.html',context)
                #ปกติ redirec เป็น javascrip (version ezy)

            newuser = User()
            newuser.username = username
            newuser.first_name = fullname
            newuser.email = email
            newuser.set_password(password)
            newuser.save()

            u = uuid.uuid1()
            token = str(u) #random uuid


            newprofile = Profile()
            newprofile.user = User.objects.get(username = username)
            newprofile.mobile = mobile
            newprofile.verify_token = token
            newprofile.save()
            text = 'กรุณากดจาก link เพื่อยืนยันการเป็นสามาชิก\n\n link : http://localhost:8000/verify-email/'+token
            sendthai(username,'Verify email (W.computer)',text)
            # context['messages'] = 'ระบบได้ส่ง email ให้คุณไปแล้วกรุณาตรวจสอบ email ล่าสุดของคุณ'
            return redirect('profile-page')
            


        try:
            user = authenticate(username = username, password=password)
            login(request,user)  
        except:    
            context['massage'] = 'username or password not correct please try again'
    return render(request, 'company/register.html',context)

def Verify_Success(request,token):
    context = {}
    try:
        check = Profile.objects.get(verify_token=token)
    # if check == Profile.objects.get(verify_token=token):
        check.verified = True
        check.save()
        check.point = 100
        return redirect('profile-page')

    except:
        context['error'] = "Link doesn't have correct ,Plase check Link in email again."
        print('end')
    return render(request, 'company/verifyemail.html',context)

@login_required
def ProfilePage(request):
    context = {}
    profileuser = Profile.objects.get(user = request.user)
    context['profile'] = profileuser
    return render(request, 'company/profile.html',context)


def ResetPassword(request):
    context = {}#สิ่งที่จะใส่เข้าไป

    if request.method == 'POST': #if กดปุ่มเข้ามา
        data = request.POST.copy()
        username = data.get('email')

        try:
            user = User.objects.get(username = username )
            u = uuid.uuid1()
            token = str(u) #random uuid
            newreset = ResetPasswordToken()
            newreset.user = user
            newreset.token = token
            newreset.save()
            text = 'กรุณากดจาก link เพื่อ reset\n\n link : http://localhost:8000/reset-new-password/'+token
            sendthai(username,'reset password link (W.computer)',text)
            context['messages'] = 'ระบบได้ส่ง email ให้คุณไปแล้วกรุณาตรวจสอบ email ล่าสุดของคุณ'

        except:  
            print('ลงมานี้')  
            context['massage'] = 'email ของคุณไม่มีในระบบ กรุณาตรวจสอบอีกครั้ง'
    return render(request, 'company/resetpassword.html',context)

def ResetNewPassword(request,token):
    context = {}
    print('token = ',token)
    check = ResetPasswordToken.objects.get(token=token)
    if check == ResetPasswordToken.objects.get(token=token):
        if request.method == 'POST': #if กดปุ่มเข้ามา
            data = request.POST.copy()
            password1 = data.get('resetpassword1')
            password2 = data.get('resetpassword2')
            if password1 == password2 :
                print('Same')
                user =check.user
                user.set_password(password1)
                user.save()
                user = authenticate(username = user.username, password=password1)
                login(request,user)
                return redirect('home-page')
            else:
                context['error'] = 'รหัสผ่านของคุณไม่ถูกต้อง กรุณาลองใหม่'
    else:
        context['error'] = "Your request code doesn't exist in the system, please check."

    return render(request, 'company/resetnewpassword.html',context)
    # try:
    #     check = ResetPasswordToken.objects.get(token=token)
    #     print('OK')
    # except:
    #         context['error'] = "Your request code doesn't exist in the system, please check."

def MyTeam (request):
    context= {}
    return render(request, 'company/team.html')

def ActionPage(request,cid):
    context = {}
    #cid = ContactList ID
    contact = ContactList.objects.get(id=cid)
    context['contact'] = contact
    try:
        action = Action.objects.get(contactlist = contact)
        context['action'] = action
    except:
        pass

    if request.method == 'POST': #if กดปุ่มเข้ามา
            data = request.POST.copy()
            detail =  data.get('detail')
            print(data)

            if 'save' in data:
                print('save data')
                try:
                    check = Action.objects.get(contactlist = contact)
                    check.actiondetail = detail
                    check.save()
                    context['action'] = check
                except:
                    new  = Action()
                    new.contactlist = contact
                    new.actiondetail = detail
                    new.save()
                    context['action'] = new

            elif 'delete' in data:
                print('Delete data')
                try:
                    check = Action.objects.get(contactlist  = contact)
                    check.delete()
                    contact.delete()
                    return redirect('accountant-page')
                except:
                    pass
            elif 'complete' in data:
                print('mark complete')
                contact.complete = True
                contact.save()
                return redirect('accountant-page')

    return render(request, 'company/action.html',context)

def AddProduct(request):

    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        description = data.get('description')
        price = data.get('price')
        quantity = data.get('quantity')
        instock = data.get('instock')

        print(title)
        print(description)
        print(price)
        print(quantity)
        print(instock)
        print("File : ",request.FILES)

        new = Product()
        new.title = title
        new.description = description
        new.price = float(price)
        new.quantity = int(quantity)

        if instock=='instock':
            new.instock = True
        
        if 'picture' in request.FILES:
            file_image = request.FILES['picture']
            file_image_name = file_image.name.replace(' ','')
            # from django.core.files.storage import FileSystemStorage
            fs = FileSystemStorage(location='media/product')
            filename = fs.save(file_image_name, file_image)
            upload_file_url = fs.url(filename)
            print('Picture URL:',upload_file_url)
            new.picture = '/product' + upload_file_url[6:]

        if 'specfile' in request.FILES:
            file_image = request.FILES['specfile']
            file_image_name = file_image.name.replace(' ','')
            # from django.core.files.storage import FileSystemStorage
            fs = FileSystemStorage(location='media/specfile')
            filename = fs.save(file_image_name, file_image)
            upload_file_url = fs.url(filename)
            print('Picture URL:',upload_file_url)
            new.specfile = '/specfile' + upload_file_url[6:]

        new.save()

    return render(request, 'company/addproduct.html')