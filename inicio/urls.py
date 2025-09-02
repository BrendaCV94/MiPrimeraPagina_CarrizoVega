from django.urls import path
from inicio.views import inicio, agregar_libro, lista_libros

urlpatterns = [
   path('', inicio, name='inicio'),
   path('libros/agregar/', agregar_libro, name='agregar_libro'),
   path('libros/', lista_libros, name='lista_libros'),
]
