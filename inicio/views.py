from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Libro
from .forms import LibroFormulario

def inicio(request):
    return render(request, 'inicio/inicio.html')

# Lista de libros
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, "inicio/lista_libros.html", {"libros": libros})

# Detalle de libro
def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    return render(request, "inicio/detalle_libro.html", {"libro": libro})

# Agregar libro (solo logueados)
@login_required(login_url='iniciar_sesion')
def agregar_libro(request):
    if request.method == "POST":
        form = LibroFormulario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro agregado correctamente.")
            return redirect("lista_libros")
    else:
        form = LibroFormulario()
    return render(request, "inicio/agregar_libro.html", {"form": form})

# Editar libro (solo logueados)
@login_required(login_url='iniciar_sesion')
def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == "POST":
        form = LibroFormulario(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado.")
            return redirect("Detalle_Libro", libro_id=libro.id)
    else:
        form = LibroFormulario(instance=libro)
    return render(request, "inicio/editar_libro.html", {"form": form, "libro": libro})

# Eliminar libro (solo logueados)
@login_required(login_url='iniciar_sesion')
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == "POST":
        libro.delete()
        messages.success(request, "Libro eliminado.")
        return redirect("lista_libros")
    return render(request, "inicio/eliminar_libro.html", {"libro": libro})

# Nueva vista
def acerca_de_mi(request):
    return render(request, "inicio/acerca_de_mi.html")
