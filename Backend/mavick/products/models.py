from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f'Categoria {self.id} : {self.nombre}'

class Talla(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f'Talla {self.id} : {self.nombre}'
        
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.BigIntegerField()
    fecha = models.DateTimeField(auto_now=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    talla = models.ManyToManyField(Talla)
    categoria = models.ManyToManyField(Categoria)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - ${self.precio} - En Stock {self.cantidad}'