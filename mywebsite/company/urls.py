from django.urls import path
from .views import *
urlpatterns = [
    path('', Home,name= 'home-page'),
    path('about/', Aboutus,name = 'about-page'), #www.W.cpmputer.com/about/
    path('contact/', ContactUs,name = 'contact-page'), #www.W.cpmputer.com/contact
]