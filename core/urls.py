from django.urls import path
from .views import inicio, login, poblar_bd, Usuario
from . import views


urlpatterns = [
    path('', inicio, name="inicio"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('inicio/', views.inicio, name="inicio"),
    path('', login, name="login"),
    path('login/', views.login, name="login" ),
     path('Usuario/<action>/<id>', Usuario, name="Usuario"),
]