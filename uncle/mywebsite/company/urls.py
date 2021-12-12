from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home-page'), # localhost:8000/
    path('about/', AboutUs, name='about-page'), # www.uncle-engineer.com/about/
    path('contact/', ContactUs, name='contact-page'),


]