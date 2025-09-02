from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroFormulario

def inicio(request):
    return render(request, 'inicio/inicio.html')

def agregar_libro(request):
    if request.method == "POST":
        form = LibroFormulario(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            libro = Libro(
                titulo=info['titulo'],
                autor=info['autor'],
                año=info['año']
            )
            libro.save()
            return redirect('lista_libros')
    else:
        form = LibroFormulario()
    return render(request, "inicio/agregar_libro.html", {"form": form})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, "inicio/lista_libros.html", {"libros": libros})

