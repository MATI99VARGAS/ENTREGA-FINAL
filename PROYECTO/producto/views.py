from django.shortcuts import render, redirect
from django import forms
from . import forms, models 
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView,UpdateView,DeleteView
import os
from django.conf import settings

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

    
class productocategoria_create(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    template_name = "producto/productocategoria_create.html"
    success_url = reverse_lazy("producto:Home")

    def test_func(self):
        return self.request.user.is_superuser 

    def handle_no_permission(self):
        return redirect("producto:Error_view") 
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)
    
class Error_view(TemplateView):
    template_name="producto/ERROR.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        error_image_path = os.path.join(settings.MEDIA_URL,'acceso_denegado.jpg')
        context[error_image_path]=error_image_path  
        return context

class producto_create(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = models.Producto
    form_class = forms.Producto_CreateForm
    template_name = "producto/producto_create.html"
    success_url = reverse_lazy("producto:buscador_productos")
    
    def test_func(self):
        return self.request.user.is_superuser 

    def handle_no_permission(self):
        return redirect("producto:Error_view")
    
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)
    

def productos_caracteristicas(request,fk):
    productos = models.Producto.objects.filter(categoria=fk)
    context = {"productos": productos}
    return render(request, "Producto/productos_caracteristicas.html", context)


class producto_update(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = models.Producto
    form_class = forms.Producto_CreateForm
    template_name = "producto/producto_update.html"
    success_url = reverse_lazy("producto:buscador_productos")

    def test_func(self):
        return self.request.user.is_superuser 

    def handle_no_permission(self):
        return redirect("producto:Error_view")
    
   

class producto_delete(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model=models.Producto
    template_name = "producto/producto_delete.html"
    success_url = reverse_lazy("producto:buscador_productos")
    def test_func(self):
        return self.request.user.is_superuser 

    def handle_no_permission(self):
        return redirect("producto:Error_view")


from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy


class producto_categoria_delete(UserPassesTestMixin, LoginRequiredMixin,DeleteView):
    model = models.ProductoCategoria
    template_name = "producto/producto_categoria_delete.html"
    success_url = reverse_lazy("producto:buscador_productos")
    def test_func(self):
        return self.request.user.is_superuser 

    def handle_no_permission(self):
        return redirect("producto:Error_view")

class producto_categoria_update(UserPassesTestMixin, LoginRequiredMixin,UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    template_name = "producto/producto_categoria_update.html"
    success_url = reverse_lazy("producto:buscador_productos")
    def test_func(self):
        return self.request.user.is_superuser 

    def handle_no_permission(self):
        return redirect("producto:Error_view")
    
    
    

    
