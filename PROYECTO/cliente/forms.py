from django import forms
from . import models

class Clientes_form(forms.ModelForm):
    class Meta:
        model = models.cliente
        fields ="__all__"
