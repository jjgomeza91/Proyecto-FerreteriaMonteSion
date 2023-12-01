from django.contrib import admin
from compras.models import Proveedor, Producto, Bodega, Compra,BodegaProducto
# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(BodegaProducto)

admin.site.register(Bodega)
admin.site.register(Compra)