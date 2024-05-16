from django.urls import path
from .views import inicio, iniciosesion, login_view, logout_view
from . import views
from django.contrib import admin

urlpatterns = [
    path('', inicio, name="inicio"),
    path('', iniciosesion, name="iniciosesion"),
    path('iniciosesion', views.login_view, name="iniciosesion" ),
     path('registro/', views.registro, name="registro"), # URL para la vista de inicio de sesión
    path('logout/', logout_view, name="logout"),
    path('admin',admin.site.urls),
]