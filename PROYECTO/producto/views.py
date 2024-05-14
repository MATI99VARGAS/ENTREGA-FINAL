from django.shortcuts import render, redirect
from django import forms
from . import forms, models 

def home(request):
    consulta_productos = models.ProductoCategoria.objects.all()
    context = {"productos":consulta_productos}
    return render(request,"producto/index.html",context)


def home_1(request):
    consulta = request.GET.get("consulta", None)
    
    if consulta:
        query = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
    else:
        query = models.ProductoCategoria.objects.all()

    context = {"productos":query}
    return render(request,"producto/buscador_productos.html",context)


def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect("producto:Home")
    else:
        form = forms.ProductoCategoriaForm()      
    return render(request, "Producto/productocategoria_create.html",context={"form":form})


def producto_create(request):
    if request.method == "POST":
        form = forms.Producto_CreateForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect("producto:Home")
    else:
        form = forms.Producto_CreateForm()
    return render(request,"Producto/producto_create.html",context = {"form":form})
    

def productos_caracteristicas(request,fk):
    productos = models.Producto.objects.filter(categoria=fk)
    context = {"productos": productos}
    return render(request, "Producto/productos_caracteristicas.html", context)



def producto_update(request,pk:int):
    query = models.Producto.objects.get(id=pk)
    if request.method == "POST":
        form = forms.Producto_CreateForm(request.POST, instance=query)
        if form. is_valid():
            form.save()
            return redirect("producto:buscador_productos")
    else:
        form = forms.Producto_CreateForm(instance=query)
    return render(request,"Producto/producto_update.html",context = {"form":form})



def producto_delete(request,pk:int):
    query = models.Producto.objects.get(id=pk)
    if request.method == "POST":
            query.delete()
            return redirect("producto:buscador_productos")
    return render(request,"Producto/producto_delete.html",context = {"form":query})


from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

class producto_categoria_delete(DeleteView):
    model = models.ProductoCategoria
    template_name = "producto/producto_categoria_delete.html"
    success_url = reverse_lazy("producto:buscador_productos")

class producto_categoria_update(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    template_name = "producto/producto_categoria_update.html"
    success_url = reverse_lazy("producto:buscador_productos")

    
