from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver

def iniciar_sesion(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            return redirect("inicio")
    else:
        formulario = AuthenticationForm()

    return render(request, 'usuarios/iniciar_sesion.html', {'formulario': formulario})


@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.success(request, "¡Cerraste sesión correctamente!")

