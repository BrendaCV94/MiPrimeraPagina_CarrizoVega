from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, EditarPerfilForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import EditarContraseñaForm
from usuarios.models import DatosExtra

def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # Crear perfil extra vacío
            DatosExtra.objects.create(user=usuario)
            login(request, usuario)  # lo loguea directo después de registrarse
            messages.success(request, "Registro exitoso.")
            return redirect("inicio")
        else:
            messages.error(request, "Por favor revisa los errores.")
    else:
        form = RegistroUsuarioForm()
    return render(request, "usuarios/registro.html", {"form": form})


def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, f"Bienvenido, {usuario.username}.")
            return redirect("inicio")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, "usuarios/iniciar_sesion.html", {"form": form})


def cerrar_sesion(request):
    logout(request)
    messages.info(request, "Sesión cerrada.")
    return redirect("inicio")



@login_required(login_url='iniciar_sesion')
def perfil(request):
    datos_extra, creado = DatosExtra.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = EditarPerfilForm(request.POST, instance=request.user)
        avatar_form = None
        if request.FILES.get("avatar"):  # Si subió un archivo
            datos_extra.avatar = request.FILES["avatar"]
            datos_extra.save()

        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("perfil")
    else:
        form = EditarPerfilForm(instance=request.user)

    return render(request, "usuarios/perfil.html", {
        "form": form,
        "datos_extra": datos_extra,
    })

class EditarContraseñaView(PasswordChangeView):
    template_name = "usuarios/editar_contraseña.html"
    form_class = EditarContraseñaForm
    success_url = reverse_lazy("perfil")