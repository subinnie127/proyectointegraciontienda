from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Empleado, Cliente
from django.contrib.auth import get_user_model
from .models import Prenda
 
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ClienteCreationForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = ('email', 'nombre', 'apellido', 'direccion', 'password1', 'password2')
class PrendaForm(forms.ModelForm):
    class Meta:
        model = Prenda
        fields = ['nombre', 'categoria', 'marca', 'descripcion', 'talla', 'precio', 'stock', 'disponible', 'imagen']