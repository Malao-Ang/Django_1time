from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    usertype = models.CharField(max_length=100,default='member')
    point = models.IntegerField(default=0)
    mobile = models.CharField(max_length=20,null=True,blank=True)
    verified = models.BooleanField(default=False)
    verify_token = models.CharField(max_length = 50,default = 'No token')

    def __str__(self):
        return self.user.username

#ดึงข้อมูลมาจาก user


# product 
#     - title (Char)
#     - descrption (text)
#     - price (int)
#     - quantity (Int)

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits = 10,decimal_places=2,null=True,blank=True)
    quantity = models.IntegerField(default=1,null=True,blank=True)
    instock = models.BooleanField(default= True)
    #file
    picture = models.ImageField(upload_to = 'product',null = True,blank=True)
    specfile = models.FileField(upload_to = 'specfile',null = True,blank=True)

    def __str__(self):
        return self.title

# รัน 2 อันนี้ทุกครั้งที่มีการเปลี่ยนแปลง Modal
# python manage.py makemigrations
# python manage.py migrate

class ContactList(models.Model):
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)
    complete  = models.BooleanField(default=False) #บอกว่าเราจัดการกับรายการนี้เรียบร้อยแล้ว
    #จะเก็ยรายการนี้

    def __str__(self):
        return self.title

class ResetPasswordToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    def __int__(self):
        return self.user.username

class Action(models.Model):
    contactlist = models.ForeignKey(ContactList,on_delete = models.CASCADE)
    actiondetail = models.TextField() #ไม่ใส่ null = True,blank=True คือให้บังคับกรอก

    def __str__(self):
        return "{} | title : {}".format(self.contactlist.email,self.contactlist.title)

