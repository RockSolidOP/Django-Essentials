"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from re import template
from django.contrib.auth import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from home import views
urlpatterns = [    
    path('', views.HomeView.as_view(), name= 'home.index' ),
    
    path('login/', views.LoginContribView.as_view(), name='home.login'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='home.logout'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('updateProfile/', views.EditProfile.as_view(), name='home.edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='home/registration/change-password.html'),name='home.change_password'),
]
