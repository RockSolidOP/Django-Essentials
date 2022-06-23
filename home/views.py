from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import datetime
from .forms import CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,DetailView,ListView
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm

from notes.models import Notes
# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/registration/register.html'
    success_url = '/notes'

    def get(self, request, *args, **kwargs):
        
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class EditProfile(UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'home/editProfile.html'
    success_url = '/notes'

    def get_object(self):
        return self.request.user

class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'home/registration/change-password.html'
    success_url = '/notes'



class LoginContribView(LoginView):
    template_name = 'home\login.html'
    success_url = ''

class LogoutInterfaceView(LogoutView):
    template_name = 'home\logout.html'
    

class HomeView(ListView):
    template_name = "home\welcome.html"
    model = Notes
    extra_context =  {'time' : datetime.now()}
    


class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = "home\\authorized.html"
    login_url = '/admin'

# def home(request):
#     return render(request=request, template_name="home\welcome.html",context= {'time' : datetime.now()})


# @login_required(login_url="/admin")
# def authorized(request=request):
#     return  render (request=request, template_name="home\\authorized.html", context= {})

