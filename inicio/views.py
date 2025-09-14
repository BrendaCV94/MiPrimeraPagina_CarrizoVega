from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .models import Libro
from .forms import LibroFormulario


def inicio(request):
    return render(request, 'inicio/inicio.html')


def agregar_libro(request):
    if request.method == "POST":
        form = LibroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroFormulario()
    return render(request, "inicio/agregar_libro.html", {"form": form})


def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, "inicio/lista_libros.html", {"libros": libros})


def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    return render(request, "inicio/detalle_libro.html", {"libro": libro})


class ActualizarLibro(UpdateView):
    model = Libro
    form_class = LibroFormulario
    template_name = "inicio/actualizar_libro.html"
    success_url = reverse_lazy("lista_libros")


class EliminarLibro(DeleteView):
    model = Libro
    template_name = "inicio/eliminar_libro.html"
    success_url = reverse_lazy("lista_libros")

