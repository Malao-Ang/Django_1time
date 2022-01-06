from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(ContactList)
admin.site.register(Profile)
admin.site.register(ResetPasswordToken)