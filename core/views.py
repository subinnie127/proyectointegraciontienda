from django.shortcuts import render, redirect
from .forms import UsuarioForm, ClienteRegistroForm
from django.views.generic import CreateView
from .models import Usuario
from django.urls import reverse_lazy
from django.contrib import messages


def inicio (request):
     return render (request, "core/inicio.html")
def iniciosesion (request):
     return render(request, "core/iniciosesion.html")
def registro (request):
     return render(request, "core/registro.html")

def Usuario(request, action, id):
    data = {"mesg": "", "form": UsuarioForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = UsuarioForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El usuario fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos usuarios con el mismo mismo mail!"

    elif action == 'upd':
        objeto = Usuario.objects.get(email=id)
        if request.method == "POST":
            form = UsuarioForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El usuario fue actualizado correctamente!"
        data["form"] = UsuarioForm(instance=objeto)

    elif action == 'del':
        try:
            Usuario.objects.get(email=id).delete()
            data["mesg"] = "¡El Usuario fue eliminado correctamente!"
            return redirect(Usuario, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El Usuario ya estaba eliminado!"

    data["list"] = Usuario.objects.all().order_by('email')
    return render(request, "core/admin.html", data)


def poblar_bd(request):
   
    return redirect(Usuario, action='ins', id = '-1')

class ClienteRegistroView(CreateView):
    form_class = ClienteRegistroForm
    template_name = 'core/registro.html'
    success_url = reverse_lazy('iniciosesion')

    def form_valid(self, form):
        # Acceder al tipo de usuario del formulario
        tipo_de_usuario = form.instance.tipo_de_usuario
        # Validar que el tipo de usuario sea "Cliente"
        if tipo_de_usuario != 'Cliente':
            # Agregar mensaje de error al campo tipo_de_usuario
            form.add_error('tipo_de_usuario', 'Solo se permite el registro de clientes.')
            # Retornar formulario inválido
            return self.form_invalid(form)
        
        # Si el tipo de usuario es "Cliente", guardar el formulario y el usuario
        self.object = form.save()

        # Agregar mensaje de éxito
        messages.success(self.request, 'Usuario registrado exitosamente.')

        # Mensaje de depuración para verificar que el usuario se ha guardado
        print("Usuario guardado correctamente:", self.object)

        return super().form_valid(form)