from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "producto"

urlpatterns = [
    path("",login_required(views.home),name="Home"),
    path("productocategoria/create/",views.productocategoria_create.as_view(),name="productocategoria_create"),

    path("productos_buscador_categoria/",login_required(views.home_1),name="buscador_productos"),
    
    path("productos_caracteristicas/<int:fk>",views.productos_caracteristicas,name="productos_caracteristicas"),
    
    path("producto_update/<int:pk>",views.producto_update.as_view(),name="producto_update"), 
    
    path("producto_create/",views.producto_create.as_view(),name="producto_create"),
    
    path("producto_delete/<int:pk>",views.producto_delete.as_view(),name="producto_delete"),
    
    path("producto_categoria_delete/<int:pk>",views.producto_categoria_delete.as_view(),name="producto_categoria_delete"),
    
    path("producto_categoria_update/<int:pk>",views.producto_categoria_update.as_view(),name="producto_categoria_update"), 

    path("error/",views.Error_view.as_view(),name="Error_view"),

]