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

from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

def cliente_delete(request,pk:int):
    query = models.cliente.objects.get(id=pk)
    if request.method == "POST":
            query.delete()
            return redirect("cliente:Home")
    return render(request,"cliente/cliente_delete.html",context = {"form":query})

class cliente_update(UpdateView):
    model = models.cliente
    form_class = forms.Clientes_form
    template_name = "cliente/cliente_update.html"
    success_url = reverse_lazy("cliente:Home")



    
 