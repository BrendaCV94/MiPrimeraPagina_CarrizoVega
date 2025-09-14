from django.urls import path
from usuarios.views import iniciar_sesion
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('cerrar-sesion/', LogoutView.as_view(), name="cerrar_sesion"),
]
