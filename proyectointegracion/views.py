from django.http import HttpResponse
from django.shortcuts import redirect, render
#request: realizar peticiones
#httpResponse: para enviar la respuesta usando http

def inicio (request):
     return render (request, "core/inicio.html")
def login (request):
     return render (request, "core/login.html")
