from django.db import models



class TipoProducto(models.Model):
  nombreTipo  = models.CharField(max_length=30);

  def __str__(self):
    return self.nombreTipo
    

class Producto(models.Model):
  nombre      = models.CharField(max_length=30)
  descripcion = models.CharField(max_length=60)
  precio      = models.IntegerField()
  stock       = models.IntegerField()
  imagen      = models.ImageField(null=True,blank=True)
  tipo        = models.ForeignKey(TipoProducto, on_delete=models.CASCADE) 

  def __str__(self):
    return self.nombre


