from django import forms
from .models import Libro
import datetime

class LibroFormulario(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'año']
        widgets = {
            'año': forms.NumberInput(attrs={'min': 0, 'max': datetime.date.today().year})
        }

    def clean_año(self):
        año = self.cleaned_data.get('año')
        current_year = datetime.date.today().year
        if año is None:
            raise forms.ValidationError("Este campo es obligatorio.")
        if año < 0:
            raise forms.ValidationError("El año no puede ser negativo.")
        if año > current_year:
            raise forms.ValidationError(f"El año no puede ser mayor que {current_year}.")
        return año
