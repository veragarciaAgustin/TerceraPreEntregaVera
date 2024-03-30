from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from app.forms import ProductoForm, ClienteForm, EmpleadoForm
from app.models import Producto, Cliente, Empleado

# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, "pagina/index.html")


def buscar_objetos(request):
    productos = []
    clientes = []
    empleados = []

    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre_producto = request.POST.get('nombre_producto', '')
        nombre_cliente = request.POST.get('nombre_cliente', '')
        nombre_empleado = request.POST.get('nombre_empleado', '')

        # Realizar la búsqueda en las respectivas tablas si los campos no están vacíos
        if nombre_producto:
            productos = Producto.objects.filter(nombre__icontains=nombre_producto)
        if nombre_cliente:
            clientes = Cliente.objects.filter(nombre__icontains=nombre_cliente)
        if nombre_empleado:
            empleados = Empleado.objects.filter(nombre__icontains=nombre_empleado)

        # Renderizar la plantilla con los resultados
        return render(request, "pagina/resultados_busqueda.html", {
            'productos': productos,
            'clientes': clientes,
            'empleados': empleados
        })
    else:
        return render(request, "pagina/formulario_busqueda.html")


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('inicio')  
    else:
        form = ProductoForm()
    return render(request, 'pagina/productos.html', {'form': form})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            empleado = form.save(commit=False)
            empleado.save()
            return redirect('inicio')  
    else:
        form = EmpleadoForm()
    return render(request, 'pagina/empleados.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('inicio')  
    else:
        form = ClienteForm()
    return render(request, 'pagina/clientes.html', {'form': form})