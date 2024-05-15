from django.shortcuts import render
from .forms import CustomAuthenticationForm
from . import models
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from . import forms

def home(request):
    return render(request,"core/index.html")

class CustomLoginView(LoginView):
    AuthenticationForm = CustomAuthenticationForm
    template_name = "core/login.html"

def register(request: HttpRequest)-> HttpResponse:
    if request.method == "POST":
        form = forms.Propio_UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request,"core/index.html",context={"mensaje":"USUARIO CREADO"})
    else:
        form = forms.Propio_UserRegisterForm()
    return render(request,"core/register.html",context={"form":form})





