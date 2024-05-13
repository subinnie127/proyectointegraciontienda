from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.hashers import make_password



class Usuario(AbstractUser):
    email =  models.EmailField(unique=True, primary_key=True)
    nombre = models.CharField( max_length=80, blank=False, null=False, verbose_name="nombre")
    apellido = models.CharField( max_length=80, blank=False, null=False, verbose_name="nombre")
    
    TIPO_DE_USUARIO =(
        ('Cliente','Cliente'),
        ('Bodeguero','Bodeguero'),
        ('Cajero','Cajero'),
    )
    tipo_de_usuario = models.CharField(
        max_length=40,
        blank=False, null=False,
        verbose_name="tipo de usuario",
        choices=TIPO_DE_USUARIO
    )
    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_permissions')

    def save(self, *args, **kwargs):
        # Utiliza el campo rut como username
        self.username = self.email

        # Hashea y guarda la contraseña de manera segura
        self.password = make_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.email