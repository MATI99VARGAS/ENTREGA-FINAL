from django import forms
from . import models

class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ProductoCategoria
        fields = "__all__"

class Producto_CreateForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"




