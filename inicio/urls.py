from django.urls import path
from inicio.views import (
    inicio,
    agregar_libro,
    lista_libros,
    detalle_libro,
    ActualizarLibro,
    EliminarLibro,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('libros/agregar/', agregar_libro, name='agregar_libro'),
    path('libros/', lista_libros, name='lista_libros'),
    path('libros/<int:libro_id>/', detalle_libro, name='Detalle_Libro'),
    path('libros/<int:pk>/editar/', ActualizarLibro.as_view(), name='Actualizar_Libro'),
    path('libros/<int:pk>/eliminar/', EliminarLibro.as_view(), name='Eliminar_Libro'),
]
