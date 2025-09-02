from django import forms

class LibroFormulario(forms.Form):
    titulo = forms.CharField(max_length=100, label="Título")
    autor = forms.CharField(max_length=100, label="Autor")
    año = forms.IntegerField(label="Año de publicación")