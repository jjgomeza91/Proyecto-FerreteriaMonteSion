from django.forms import ModelForm
from compras.models import *


class ProveedorForm(ModelForm):
    class Meta:
        model= Proveedor
        fields= "__all__"
        exclude=["estado",]

class ProductoForm(ModelForm):
    class Meta:
        model= Producto
        fields= "__all__"
        exclude=["estado",]

class BodegaForm(ModelForm):
    class Meta:
        model= Bodega
        fields= "__all__"
        exclude=["estado",]

class CompraForm(ModelForm):
    
    class Meta:
        model= Compra
        fields= "__all__"
        exclude=["estado","fecha"]

class CompraDetalleForm(ModelForm):
    
    class Meta:
        model= CompraDetalle
        fields= ["producto","cantidad"]

    def __init__(self, *args, **kwargs):
            super(CompraDetalleForm, self).__init__(*args, **kwargs)

            # Agregar la clase "select" al campo "producto"
            self.fields['producto'].widget.attrs['class'] = 'select w-50'
            
        