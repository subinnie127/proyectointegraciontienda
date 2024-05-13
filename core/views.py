from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario

def inicio (request):
     return render (request, "core/inicio.html")
def iniciosesion (request):
     return render(request, "core/iniciosesion.html")

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