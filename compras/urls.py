from django.urls import path
from compras.views import *

urlpatterns = [
    path('proveedores/', proveedores, name='proveedores'),
    path('proveedores/nuevo/', proveedor_crear, name='proveedores_crear'),
    path('productos/', productos, name='productos'),
    path('productos/nuevo/', producto_crear, name='productos_crear'),
    path('bodegas/', bodegas, name='bodegas'),
    path('bodegas/nuevo/', bodega_crear, name='bodegas_crear'),
    path('', compra, name='compras'),
    path('eliminar/<int:compra_id>/', compra_eliminar, name='compra_eliminar'),

    path('nuevo/', compra_crear, name='compra_crear'),
    path('detalle/<int:compra_id>/', compra_detalle, name='compra_detalle'),
    path('detalle/eliminar/<int:compra_id>/<int:detalle_id>/', compra_detalle_eliminar, name='compra_detalle_eliminar'),
    path('cerrar/<int:compra_id>/', compra_cerrar, name='compra_cerrar'),



]

