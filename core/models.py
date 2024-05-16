from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class ClienteManager(BaseUserManager):
    def create_user(self, email, nombre, apellido, direccion, password=None):
        if not email:
            raise ValueError('El correo electrónico debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, apellido=apellido, direccion=direccion)
        user.set_password(password)
        user.save(using=self._db)
        return user
class Cliente(AbstractBaseUser):
    email = models.EmailField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ClienteManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'direccion']

    def __str__(self):
        return self.email
