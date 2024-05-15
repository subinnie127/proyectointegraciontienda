from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido', 'tipo_de_usuario']

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

class ClienteRegistroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ['email', 'nombre', 'apellido', 'direccion']

    def clean(self):
        cleaned_data = super().clean()
        tipo_de_usuario = 'Cliente'  # Asumiendo que solo los clientes pueden registrarse con este formulario
        if cleaned_data.get("tipo_de_usuario") != tipo_de_usuario:
            raise forms.ValidationError("Solo se permite el registro de clientes.")
