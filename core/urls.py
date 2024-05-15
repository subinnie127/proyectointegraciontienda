from django.urls import path
from django.views.generic import CreateView
from .views import inicio, Usuario, iniciosesion, registro,  ClienteRegistroView, IniciarSesionView
from . import views
from django.contrib import admin

urlpatterns = [
    path('', inicio, name="inicio"),
    path('inicio/', views.inicio, name="inicio"),
    path('', iniciosesion, name="iniciosesion"),
    path('iniciosesion', IniciarSesionView.as_view(), name="iniciosesion" ),
    path('Usuario/<action>/<id>', Usuario, name="Usuario"),
    path('admin',admin.site.urls),
        path('', registro, name="registro"),
    path('registro', ClienteRegistroView.as_view(), name="registro" ),
]