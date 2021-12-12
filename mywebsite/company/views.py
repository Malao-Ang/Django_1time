from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from songline import Sendline


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
        token = 'WuJJobc3Xr0vdnrULjqY4UTvI1BxNrspbKUgpmLUaBL'

            # token สามารถสมัคร+ยกเลิกได้ผ่านทาง line notify

        m = Sendline(token)
        m.sendtext('\ntitle:{} \nemail:{} \n>>>{}'.format(title,email,detail))
        #บันทึกข้อมูล
        #ทำให้เหลือบรรทัดเดียว
        #ContactList(title=newrecord.title, email=newrecord.email).save()

    return render(request, 'company/contact.html',context)

from django.contrib.auth import authenticate,login
def Login(request):
    context = {}#สิ่งที่จะใส่เข้าไป

    if request.method == 'POST': #if กดปุ่มเข้ามา
        data = request.POST.copy()
        username = data.get('username')
        password = data.get('password')

        try:
            user = authenticate(username=username, password=password)
            login(request,user)  
        except:    
            context['massage'] = 'username or password not correct please try again'
    return render(request, 'company/login.html',context)


