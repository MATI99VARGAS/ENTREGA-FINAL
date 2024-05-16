from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class vendedor(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE,related_name="vendedor")
    celular = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatares",null=True,blank=True)

    def __str__(self) -> str:
        return self.usuario.username
    
class Venta(models.Model):
    vendedor = models.ForeignKey(vendedor,on_delete=models.DO_NOTHING)
    producto = models.ForeignKey("producto.Producto",on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10,decimal_places=2,editable=False)
    fecha_venta = models.DateField(default=timezone.now, editable=False)
    
    class Meta:
        ordering = ("-fecha_venta",)
    
    def save(self,*args,**kwars):
        self.precio_total = self.producto.precio_producto * self.cantidad
        super().save(*args,**kwars)