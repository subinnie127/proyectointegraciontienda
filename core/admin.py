from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Cliente, Categoria, Marca, Prenda, Pedido, ItemPedido, Cargo, Empleado
class ClienteAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'nombre', 'apellido', 'direccion']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('nombre', 'apellido', 'direccion')}),
        ('Fechas importantes', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'apellido', 'direccion', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'nombre', 'apellido', 'direccion')
    list_filter = ('is_active', 'is_staff') 
    filter_horizontal = ()

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Prenda)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Cargo)
admin.site.register(Empleado)