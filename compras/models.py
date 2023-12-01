from django.db import models
from django.utils.translation import gettext_lazy as _

def get_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.id}-{instance.nombre_producto}.{ext}"
    return f"compras/productos/{filename}"

class Proveedor(models.Model):
    nombre_proveedor= models.CharField(max_length=45,verbose_name="Nombre proveedor")

    class TipoDocumento(models.TextChoices):
        CEDULA='CC',_("Cédula")
        NIT='NI',_("Nit")
    tipo_documento= models.CharField(max_length=2,choices=TipoDocumento.choices,verbose_name="Tipo documento")
    
    documento= models.PositiveIntegerField(verbose_name="Número documento", unique=True)
    ciudad= models.CharField(max_length=45,verbose_name="Ciudad")
    direccion= models.CharField(max_length=45,verbose_name="Dirección")
    telefono= models.PositiveIntegerField(verbose_name="Teléfono")
    
    nombre_contacto= models.CharField(max_length=45,verbose_name="Nombre contacto")
    telefono_contacto= models.PositiveIntegerField(verbose_name="Teléfono contacto")

    estado= models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_proveedor
    class Meta:
        verbose_name_plural="Proveedores"

class Bodega(models.Model):
    nombre_bodega= models.CharField(max_length=45,verbose_name="Nombre bodega")
    descripcion_bodega= models.CharField(max_length=200,verbose_name="Descripción bodega")
    estado= models.BooleanField(default=True)

class Producto(models.Model):
    nombre_producto= models.CharField(max_length=45,verbose_name="Nombre producto")
    unidad_medida= models.CharField(max_length=45,verbose_name="Unidad medida")
    stock_minimo= models.PositiveIntegerField(verbose_name="Stock mínimo")
    precio_unitario_compra= models.PositiveIntegerField(verbose_name="Precio unitario compra")
    precio_unitario_venta= models.PositiveIntegerField(verbose_name="Precio unitario venta")
    imagen = models.ImageField(upload_to=get_image_filename, blank=True, null=True,default="compras/imagenProducto.jpg")
    estado= models.BooleanField(default=True)
    def __str__(self):
        return f"{self.id} {self.nombre_producto}"
    


class BodegaProducto(models.Model):
    producto= models.ForeignKey(Producto, verbose_name="Producto", on_delete=models.CASCADE)
    bodega= models.ForeignKey(Bodega, verbose_name="Bodega", on_delete=models.CASCADE)
class Compra(models.Model):
    codigo=models.CharField(max_length=15, verbose_name="Código de Factura")
    fecha= models.DateTimeField( auto_now=True)
    descuento= models.PositiveIntegerField(verbose_name="Descuento", default=0)
    class Estado(models.TextChoices):
        ABIERTA='1',_("Abierta")
        ANULADA='2',_("Anulada")
        CERRADA='0',_("Cerrada")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ABIERTA,verbose_name="Estado")
    observaciones= models.TextField(verbose_name="Observaciones", blank=True, null=True)
    proveedor=models.ForeignKey(Proveedor, verbose_name="Proveedor", on_delete=models.CASCADE)
    
class CompraDetalle(models.Model):
    compra= models.ForeignKey(Compra, verbose_name="Compra", on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto, verbose_name="Producto", on_delete=models.CASCADE)
    cantidad= models.PositiveIntegerField(verbose_name="Cantidad",default=1)



