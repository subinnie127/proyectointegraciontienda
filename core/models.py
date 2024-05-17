from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.exceptions import ValidationError
from django.db import models
import re

def validar_rut(value):
    rut_regex = re.compile(r'^\d{1,8}-[0-9Kk]$')
    if not rut_regex.match(value):
        raise ValidationError('El RUT debe tener el formato XXXXXXXX-X')

    # Validar dígito verificador
    rut, dv = value.split('-')
    rut = int(rut)
    suma = 0
    factor = 2

    for digit in reversed(str(rut)):
        suma += int(digit) * factor
        factor = 9 if factor == 7 else factor + 1

    calculated_dv = 11 - (suma % 11)
    if calculated_dv == 11:
        calculated_dv = '0'
    elif calculated_dv == 10:
        calculated_dv = 'K'
    else:
        calculated_dv = str(calculated_dv)

    if calculated_dv.upper() != dv.upper():
        raise ValidationError('El dígito verificador del RUT no es válido')
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
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Prenda(models.Model):
    TALLAS = [
        ('XS', 'Extra Pequeño'),
        ('S', 'Pequeño'),
        ('M', 'Mediano'),
        ('L', 'Grande'),
        ('XL', 'Extra Grande'),
    ]

    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    talla = models.CharField(max_length=2, choices=TALLAS)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='imagenes_prendas/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.talla}) - {self.precio}"
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    prendas = models.ManyToManyField(Prenda, through='ItemPedido')
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    prenda = models.ForeignKey(Prenda, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.prenda.nombre} - {self.pedido}"
class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True, validators=[validar_rut])
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"