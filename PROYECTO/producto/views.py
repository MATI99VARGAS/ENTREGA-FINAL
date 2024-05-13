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

def Producto_create(request):
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



def productocategoria_update(request,pk):
    query = models.Producto.objects.get(pk)
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST, instance=query)
        if form. is_valid():
            form.save()
            return redirect("producto:Home")
    else:
        form = forms.ProductoCategoriaForm()      
    return render(request, "Producto/productocategoria_create.html",context={"form":form})

