from django import forms
from .models import Libro

class LibroFormulario(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'año']
