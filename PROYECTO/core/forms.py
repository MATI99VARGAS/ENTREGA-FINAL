from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User, Group, Permission




class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username","password"]
        widgets = {
            "username":forms.TextInput(attrs={"class":"form-control"}),

            "password":forms.PasswordInput(attrs={"class":"form-control"}),

        }

class Propio_UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name= forms.CharField(label = "Apellido")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
      model = User
      fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
      help_texts = {k:"" for k in fields}
    
    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            CLIENTES_NUEVOS_group = Group.objects.get(name="CLIENTES_NUEVOS")
            user.groups.add(CLIENTES_NUEVOS_group)
        return user
