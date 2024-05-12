from django.contrib import admin

from . import models

admin.site.register(models.ProductoCategoria)
admin.site.register(models.Origen)
admin.site.register(models.Producto)