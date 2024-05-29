from django.urls import path
from .views import inicio, iniciosesion, login_view, logout_view, ClienteCreationForm
from . import views
from django.contrib import admin

urlpatterns = [
    path('', inicio, name="inicio"),
    path('', iniciosesion, name="iniciosesion"),
    path('iniciosesion', views.login_view, name="iniciosesion" ),
    path('registro/', views.registro, name="registro"), # URL para la vista de inicio de sesión
    path('logout/', logout_view, name="logout"),
    path('admin',admin.site.urls),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('lista/', views.lista_productos, name='lista_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]