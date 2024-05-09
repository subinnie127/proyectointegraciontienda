from django import forms
from .models import Usuario
from django.forms import ModelForm

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido', 'tipo_de_usuario']
        widgets = {
            'password': forms.PasswordInput(), 
        }

    

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        if len(apellido) < 3:
            raise forms.ValidationError("El apellido debe tener al menos 3 caracteres.")
        return apellido

    # Resto de los métodos de limpieza


    # Métodos de limpieza para el formulario de contacto
