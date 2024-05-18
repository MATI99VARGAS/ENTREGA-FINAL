from django.contrib import admin

from . import models

admin.site.site_title = "Clientes"


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("apellido","nombre","nacimiento","pais_origen_id","nivel_sus")
    list_display_links = ("apellido",)


admin.site.register(models.Pais)
admin.site.register(models.cliente,ClienteAdmin)
admin.site.register(models.suscripcion)
