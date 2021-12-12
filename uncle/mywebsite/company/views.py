from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from songline import Sendline # pip install songline

# def Home(request):
# 	return HttpResponse('<h1>Hello World!</h1> <br> <p>by Uncle Engineer</p>')

def Home(request):
	allproduct = Product.objects.all() # SELECT * from product
	context = {'allproduct':allproduct}
	return render(request, 'company/home.html',context)


def AboutUs(request):
	return render(request, 'company/aboutus.html')


def ContactUs(request):


	context = {} #สิ่งที่จะแนบไป

	if request.method == 'POST':
		data = request.POST.copy()
		title = data.get('title')
		email = data.get('email')
		detail = data.get('detail')
		print(title)
		print(email)
		print(detail)
		print('----------------')

		# กรณีที่ user ไม่กรอกข้อมูล
		if title == '' and email == '':
			context['message'] = 'พี่ครับ รบกวนกรอกหัวข้อและอีเมลล์ด้วยครับ เพราะจะส่งคำตอบไม่ได้'
			return render(request, 'company/contact.html',context)


		# เมื่อได้ข้อมูลแล้วจะทำการบันทึกข้อมูล
		# ContactList(title=title,email=email,detail=detail).save()
		newrecord = ContactList()
		newrecord.title = title
		newrecord.email = email
		newrecord.detail = detail
		newrecord.save()
		context['message'] = 'ตอนนี้ลุงได้รับข้อความเรียบร้อยแล้ว รอลุงตอบกลับภายใน 24 ชั่วโมง'

		# ส่งไลน์ from songline import Sendline
		token = 'roGvMiezP6mTzFIL4j6eSKVUHVYRPXG238d6gpnBiyc'
		m = Sendline(token)
		m.sendtext('\nหัวข้อ:{}\nอีเมลล์:{}\n>>> {}'.format(title,email,detail))

	return render(request, 'company/contact.html',context)


from django.contrib.auth import authenticate, login

def Login(request):

	context = {} #สิ่งที่จะแนบไป

	if request.method == 'POST':
		data = request.POST.copy()
		username = data.get('username')
		password = data.get('password')

		try:
			user = authenticate(username=username, password=password)
			login(request,user)
		except:
			context['message'] = 'username หรือ password อาจไม่ถูกต้อง กรุณาติดต่อแอดมิน'

	return render(request, 'company/login.html',context)
