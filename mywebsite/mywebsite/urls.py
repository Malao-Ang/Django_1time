"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include # include คือคำสั่งไว้link ระหว่าง project กับ link

from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('company.urls')),#link ไปยังapp
    path('login/',views.LoginView.as_view(template_name='company/login.html'), name = 'login'),
    path('logout/',views.LogoutView.as_view(template_name='company/logout.html'), name = 'logout'),
]
