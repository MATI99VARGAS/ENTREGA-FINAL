from django.urls import path
from cliente import views
app_name = "cliente"

urlpatterns = [
    path("",views.home,name="Home"),
    path("cliente_create",views.cliente_create,name="cliente_create"),
    path("cliente_update/<int:pk>",views.cliente_update.as_view(),name="cliente_update"), 
    path("cliente_delete/<int:pk>",views.cliente_delete,name="cliente_delete"),
    path("cliente_detail/<int:pk>",views.cliente_detail,name="cliente_detail"),
]