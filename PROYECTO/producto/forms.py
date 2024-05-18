from django import forms
from . import models


class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ProductoCategoria
        fields = "__all__"
        widgets = {
            'imagen': forms.FileInput()
            }

class Producto_CreateForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"
        widgets = {
            'imagen': forms.FileInput()
            }




