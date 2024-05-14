from django.urls import path
from . import views
app_name = "producto"

urlpatterns = [
    path("",views.home,name="Home"),
    path("productocategoria/create/",views.productocategoria_create,name="productocategoria_create"),
    path("productos_buscador_categoria/",views.home_1,name="buscador_productos"),
    path("productos_caracteristicas/<int:fk>",views.productos_caracteristicas,name="productos_caracteristicas"),
    path("producto_update/<int:pk>",views.producto_update,name="producto_update"), 
    path("producto_create/",views.producto_create,name="producto_create"),
    path("producto_delete/<int:pk>",views.producto_delete,name="producto_delete"),
    path("producto_categoria_delete/<int:pk>",views.producto_categoria_delete.as_view(),name="producto_categoria_delete"),
    path("producto_categoria_update/<int:pk>",views.producto_categoria_update.as_view(),name="producto_categoria_update"), 
    

]