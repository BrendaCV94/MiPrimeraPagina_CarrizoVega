from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm

# Validador simple de contraseña
def validar_contraseña(valor):
    if len(valor) < 6:
        raise ValidationError("La contraseña debe tener al menos 6 caracteres.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", valor):
        raise ValidationError("Debe incluir al menos un caracter especial (!, @, #, etc).")

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        validators=[validar_contraseña]
    )
    password2 = forms.CharField(
        label="Repetir Contraseña",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Username",
        }
        help_texts = {
            "username": "", 
            "password1": "",
            "password2": "",
        }


# Validador simple de contraseña
def validar_contraseña(valor):
    if len(valor) < 6:
        raise ValidationError("La contraseña debe tener al menos 6 caracteres.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", valor):
        raise ValidationError("Debe incluir al menos un caracter especial (!, @, #, etc).")

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        validators=[validar_contraseña]
    )
    password2 = forms.CharField(
        label="Repetir Contraseña",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Username",
        }
        help_texts = {
            "username": "",
            "password1": "",
            "password2": "",
        }

# Nuevo formulario para editar perfil con UserChangeForm
class EditarPerfilForm(UserChangeForm):
    password = None  # Ocultamos el campo contraseña

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        labels = {
            "username": "Nombre de usuario",
            "email": "Correo electrónico",
            "first_name": "Nombre",
            "last_name": "Apellido",
        }
        
class EditarContraseñaForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Contraseña actual",
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="La contraseña debe tener al menos 8 caracteres y no puede ser totalmente numérica."
    )
    new_password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )