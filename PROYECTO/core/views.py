from django.shortcuts import render
from .forms import CustomAuthenticationForm
from . import models
from django.contrib.auth.views import LoginView

def home(request):
    return render(request,"core/index.html")

class CustomLoginView(LoginView):
    AuthenticationForm = CustomAuthenticationForm
    template_name = "core/login.html"





