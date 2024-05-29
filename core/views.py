from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Empleado, Cliente
from django.contrib.auth import authenticate, login, logout
from .forms import EmpleadoForm, ClienteForm, ClienteCreationForm, PrendaForm
import requests

API_URL = 'http://127.0.0.1:5000/api/productos'

def inicio(request):
    context = {
        'user': request.user}
    return render(request, "core/inicio.html", context)

def iniciosesion(request):
    context = {
        'user': request.user}
    return render(request, "core/iniciosesion.html",context)

def registro(request):
    if request.method == 'POST':
        form = ClienteCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciosesion')  # Redirige al usuario a la página de inicio de sesión después de registrarse
    else:
        form = ClienteCreationForm()
    return render(request, 'core/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Correo o contraseña incorrectos')
    return render(request, 'core/iniciosesion.html')
def logout_view(request):
    logout(request)
    return redirect('iniciosesion')

#matenedor de Usuarios de la pagina
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'core/lista_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'core/agregar_empleado.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/lista_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'core/agregar_cliente.html', {'form': form})
#integracion de api 

def lista_productos(request):
    response = requests.get(API_URL)
    productos = response.json()
    return render(request, 'core/lista_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = PrendaForm(request.POST, request.FILES)
        if form.is_valid():
            datos = form.cleaned_data
            archivos = {'imagen': request.FILES['imagen']} if 'imagen' in request.FILES else {}
            response = requests.post(API_URL, data=datos, files=archivos)
            if response.status_code == 201:
                return redirect('lista_productos')
            else:
                form.add_error(None, 'Error al crear el producto')
    else:
        form = PrendaForm()
    return render(request, 'core/crear_producto.html', {'form': form})

def editar_producto(request, id):
    producto_url = f'{API_URL}/{id}'
    if request.method == 'POST':
        form = PrendaForm(request.POST, request.FILES)
        if form.is_valid():
            datos = form.cleaned_data
            archivos = {'imagen': request.FILES['imagen']} if 'imagen' in request.FILES else {}
            response = requests.put(producto_url, data=datos, files=archivos)
            if response.status_code == 200:
                return redirect('lista_productos')
            else:
                form.add_error(None, 'Error al editar el producto')
    else:
        response = requests.get(producto_url)
        if response.status_code == 200:
            producto = response.json()
            form = PrendaForm(initial=producto)
        else:
            return redirect('lista_productos')
    return render(request, 'core/editar_producto.html', {'form': form, 'producto_id': id})

def eliminar_producto(request, id):
    producto_url = f'{API_URL}/{id}'
    response = requests.delete(producto_url)
    return redirect('lista_productos')