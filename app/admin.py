from django.contrib import admin
from app.models import Producto, Cliente, Empleado

# Register your models here.

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Empleado)