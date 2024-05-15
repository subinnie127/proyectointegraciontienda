from django.urls import path
from django.views.generic import CreateView
from .views import inicio, poblar_bd, Usuario, iniciosesion, registro,  ClienteRegistroView
from . import views
from django.contrib import admin

urlpatterns = [
    path('', inicio, name="inicio"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('inicio/', views.inicio, name="inicio"),
    path('', iniciosesion, name="iniciosesion"),
    path('iniciosesion', views.iniciosesion, name="iniciosesion" ),
    path('Usuario/<action>/<id>', Usuario, name="Usuario"),
    path('admin',admin.site.urls),
        path('', registro, name="registro"),
    path('registro', ClienteRegistroView.as_view(), name="registro" ),
]