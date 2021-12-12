from django.contrib import admin
from .models import *

admin.site.register(Product) # เป็นการทำให้แอดสามารถเห็นฐานข้อมูล
admin.site.register(ContactList) #เพิ่ม model ใหม่อีกรายการ
