from django.urls import path
from ventas.views import clientes,cliente_crear

urlpatterns = [
    path('clientes/', clientes, name='clientes'),
    path("clientes/nuevo/", cliente_crear, name="clientes_crear"),

]

