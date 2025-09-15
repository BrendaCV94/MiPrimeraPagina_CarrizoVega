from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re
from django.core.exceptions import ValidationError

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
