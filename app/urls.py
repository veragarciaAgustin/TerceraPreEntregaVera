from django.urls import path, include
from app.views import Index
from . import views


urlpatterns = [
    path('', Index.as_view(), name="inicio"),
    path('producto/', views.agregar_producto, name='agregar_producto'),
    path('cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('empleado/', views.agregar_empleado, name='agregar_empleado'),
    path('buscar/', views.buscar_objetos, name='buscar_objetos'),
]