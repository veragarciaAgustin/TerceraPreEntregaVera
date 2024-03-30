from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(decimal_places = 3, max_digits = 10)
    marca = models.CharField(max_length=255)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    puesto = models.CharField(max_length=255)
    fechaDeIngreso = models.DateField()
    
