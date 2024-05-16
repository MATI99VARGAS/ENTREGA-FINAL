from django.contrib import admin

from . import models

class VentaAdmin(admin.ModelAdmin):
    list_display = ("vendedor",
                  "producto",
                  "cantidad",
                  "precio_total",
                  "fecha_venta")
    
    list_display_links = ("producto",)

    search_fields = ("producto.nombre","vendedor")

    list_filter = ("vendedor",)
    
    date_hierarchy = "fecha_venta"






admin.site.register(models.vendedor,)

admin.site.register(models.Venta,VentaAdmin)
