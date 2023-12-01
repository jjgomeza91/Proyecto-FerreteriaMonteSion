from django.urls import path
from configuracion.views import usuarios, usuario_crear, usuario_eliminar, usuario_editar

urlpatterns = [
    path('usuarios/', usuarios, name='usuarios'),
    path("usuarios/nuevo/", usuario_crear, name="usuarios_crear"),
    path("usuarios/eliminar/<int:pk>", usuario_eliminar, name="usuario-eliminar"),
    path("usuarios/editar/<int:pk>", usuario_editar, name="usuario-editar"),
]

