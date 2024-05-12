from django.urls import path
from cliente import views
app_name = "cliente"

urlpatterns = [
    path("",views.home,name="Home"),
    path("cliente_create.html",views.cliente_create,name="cliente_create"),
    
]