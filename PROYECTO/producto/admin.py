from django.contrib import admin

from . import models

admin.site.site_title = "Productos"

class ProductoCategoiaAdmin(admin.ModelAdmin):
    list_display = ("nombre","descripcion")
    list_display_links = ("nombre",)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre","categoria","precio_producto","Origen_producto")
    list_display_links = ("nombre",)


admin.site.register(models.ProductoCategoria,ProductoCategoiaAdmin)
admin.site.register(models.Origen)
admin.site.register(models.Producto,ProductoAdmin)