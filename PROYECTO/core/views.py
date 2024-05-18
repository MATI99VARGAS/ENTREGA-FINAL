from django.shortcuts import render
from .forms import CustomAuthenticationForm
from . import models
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from . import forms
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
import os
from django.conf import settings


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
            return render(request,"core/index.html")
    else:
        form = forms.Propio_UserRegisterForm()
    return render(request,"core/register.html",context={"form":form})


class Error_view(TemplateView):
    template_name="producto/ERROR.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        error_image_path = os.path.join(settings.MEDIA_URL,'acceso_denegado.jpg')
        context[error_image_path]=error_image_path  
        return context


