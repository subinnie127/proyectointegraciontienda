from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def inicio(request):
    context = {
        'user': request.user}
    return render(request, "core/inicio.html", context)

def iniciosesion(request):
    context = {
        'user': request.user}
    return render(request, "core/iniciosesion.html",context)

def registro(request):
    context = {
        'user': request.user}
    return render(request, "core/registro.html", context)

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
