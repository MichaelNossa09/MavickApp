from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Producto

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.BigIntegerField(unique=True)
    username = None
    foto = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'''Cliente {self.id}: Email: {self.email} Password: {self.password} Nombre: {self.nombre} {self.apellido}
        Telefono {self.telefono}'''

class Direccion(models.Model):
    idClient = models.ForeignKey(User, on_delete=models.CASCADE)
    pais = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    codpostal = models.CharField(max_length=6)

    def __str__(self):
        return f'''
            Dirección {self.id}: {self.direccion} - {self.ciudad}({self.estado}) - {self.pais} - Código Postal: {self.codpostal}
        '''

class Estado(models.Model):
    estado = models.CharField(max_length=255)

    def __str__(self):
        return f'Estado {self.id}: {self.estado}'

class Carrito(models.Model):
    idClient = models.ForeignKey(User, on_delete=models.CASCADE)
    idProduct = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.idProduct.nombre} - Precio: {self.idProduct.precio} - Cantidad: {self.cantidad}'
class MetodoPago(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f'Metodo de pago {self.id}: {self.nombre}'

class Pedido(models.Model):

    idClient = models.ForeignKey(User, on_delete=models.CASCADE)
    idMetodoPago = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True)
    total = models.FloatField()
    idDireccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Pedido #{self.id}: Cliente: {self.idClient.nombre} - MetodoPago: {self.idMetodoPago.nombre} - Total: {self.total}'

class PedidoDetalle(models.Model):
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    precio = models.FloatField()

    def __str__(self):
        return f'Detalle del Pedido {self.id}: Cliente: {self.idPedido.idClient.nombre} - Precio: {self.precio} - Producto {self.idProducto.nombre}'