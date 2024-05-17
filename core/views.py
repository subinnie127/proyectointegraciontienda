from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Empleado, Cliente
from django.contrib.auth import authenticate, login, logout
from .forms import EmpleadoForm, ClienteForm, ClienteCreationForm

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
