from dataclasses import fields
import email
from faulthandler import disable
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm( UserChangeForm ):

    username  = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name  = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    last_login = forms.Field(widget=forms.TextInput(attrs={'class': 'form-control'}),disabled=True)  
    # user_permissions = forms.MultipleHiddenInput()
    # is_staff
    # is_active
   
    # user_permissions = forms.Textarea(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control' 'readonly'}))

    
    # groups
    # user_permissions
    # is_staff
    # is_active

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','last_login',)
    