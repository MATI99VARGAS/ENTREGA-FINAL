from django.db import models

class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=200,unique=True)
    descripcion = models.CharField(max_length=250,null=True, blank=True,verbose_name='descripción')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "categoría de productos"

class Origen(models.Model):
    Origen_producto= models.CharField(max_length=200,unique=True)
    def __str__(self):

     return self.Origen_producto

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, null=True, verbose_name="categoría de productos")
    precio_producto = models.PositiveBigIntegerField(verbose_name="Precio")
    Origen_producto = models.ForeignKey(Origen, on_delete=models.SET_NULL, null=True, verbose_name="Origen del producto")
    
    def __str__(self):

     return self.nombre
     
