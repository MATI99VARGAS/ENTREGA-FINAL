from django.db import models

class suscripcion(models.Model):
    nivel = models.CharField(max_length=50)
    def __str__(self):

        return self.nivel

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):

        return self.nombre
    
    class Meta:
        verbose_name_plural = 'Países'

class cliente(models.Model):
        nombre = models.CharField(max_length=200)

        apellido = models.CharField(max_length=50)

        nacimiento = models.DateField(null=True)

        pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, verbose_name="País de origen")

        nivel_sus = models.ForeignKey(suscripcion, on_delete=models.SET_NULL, null=True, verbose_name="Nivel")

        def __str__(self):
             return self.nombre

            