from django.urls import path
from .views import *
urlpatterns = [
    path('', Home,name= 'home-page'),
    path('about/', Aboutus,name = 'about-page'), #www.W.cpmputer.com/about/
    path('contact/', ContactUs,name = 'contact-page'), #www.W.cpmputer.com/contact
    path('accountant/',Accountant,name = 'accountant-page'), #www.W.computer/accuntat
    path('register/', Register,name = 'register-page'), #www.W.computer/register
    path('profile/', ProfilePage,name = 'profile-page'), #www.W.computer/profile
    path('reset-password/', ResetPassword,name = 'reset-password'), #www.W.computer/resetpassword
]