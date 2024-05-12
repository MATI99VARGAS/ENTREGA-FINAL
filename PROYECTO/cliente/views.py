from django.shortcuts import render, redirect
from django import forms
from . import models, forms

def home(request):
    consulta = request.GET.get("consulta", None)

    if consulta:
        query = models.cliente.objects.filter(nombre__icontains=consulta) 
    
    else:
        query = models.cliente.objects.all()

    context = {"clientes":query}
    
    return render(request,"cliente/index.html",context)

def cliente_create(request):
    if request.method == "POST":
        form = forms.Clientes_form(request.POST)
        if form. is_valid():
            form.save() 
            return redirect("cliente:Home")
    else:
        form = forms.Clientes_form()
    return render(request, "cliente/cliente_create.html",context={"form":form})
 