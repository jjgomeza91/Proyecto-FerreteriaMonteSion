from django.shortcuts import get_object_or_404, render, redirect
from compras.models import *
from compras.forms import *
from django.contrib import messages
from PIL import Image
from django.db.models import F, ExpressionWrapper, fields, Sum

# Create your views here.
def proveedores(request):
    titulo="Proveedores"
    proveedores = Proveedor.objects.all()
    context={
        "titulo": titulo,
        "proveedores":proveedores,
    }
    return render(request, "compras/proveedores/proveedores.html", context)

def proveedor_crear(request):
    titulo="Proveedores"
    accion="Agregar"
    if request.method=="POST":
        form= ProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            proveedor=form.save()
            proveedor.save()
            messages.success(request, f'¡El proveedor se guardó de forma exitosa!')
            return redirect('proveedores')
        else:
            messages.error(request, f'¡Error al agregar al Proveedor!')
    else:
        form=ProveedorForm()
    context={
    "titulo":titulo,
    'form':form,
    'accion':accion,
    }
    return render (request,"compras/proveedores/nuevoproveedor.html", context )

def productos(request):
    titulo="Productos"
    productos = Producto.objects.all()
    context={
        "titulo": titulo,
        "productos":productos,
    }
    return render(request, "compras/productos/productos.html", context)

def producto_crear(request):
    titulo="Productos"
    accion="Agregar"
    if request.method=="POST":
        form= ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto=form.save()
            if producto.imagen:
                img=Image.open(producto.imagen.path)
                img=img.resize((500,500))
                img.save(producto.imagen.path)
            producto.save()
            messages.success(request, f'¡El producto se guardó de forma exitosa!')
            return redirect('productos')
        else:
            messages.error(request, f'¡Error al agregar el producto!')
    else:
        form=ProductoForm()
    context={
    "titulo":titulo,
    'form':form,
    'accion':accion,
    }
    return render (request,"compras/productos/nuevoproducto.html", context )

def bodegas(request):
    titulo="Bodegas"
    proveedores = Bodega.objects.all()
    context={
        "titulo": titulo,
        "bodegas":bodegas,
    }
    return render(request, "compras/bodegas/bodegas.html", context)

def bodega_crear(request):
    titulo="Bodegas"
    accion="Agregar"
    if request.method=="POST":
        form= BodegaForm(request.POST, request.FILES)
        if form.is_valid():
            bodega=form.save()
            bodega.save()
            messages.success(request, f'¡La bodega se guardó de forma exitosa!')
            return redirect('bodegas')
        else:
            messages.error(request, f'¡Error al agregar la bodega')
    else:
        form=BodegaForm()
    context={
    "titulo":titulo,
    'form':form,
    'accion':accion,
    }
    return render (request,"compras/bodegas/nuevabodega.html", context )

def compra(request):
    titulo="Compra"
    compras= Compra.objects.all()
    context={
        "titulo":titulo,
        "compras":compras
    }
    return render(request,"compras/compra/compras.html", context)

def compra_crear(request):
    titulo="Compra"
    accion="Abrir"
    if request.method=="POST":
        form= CompraForm(request.POST)
        if form.is_valid():
            compra=form.save()
            compra.save()
            messages.success(request, f'¡La ha abierto la compra de forma exitosa!')
            return redirect('compra_detalle', compra_id=compra.id)
        else:
            messages.error(request, f'¡Error al abrir la compra')
    else:
        form=CompraForm()
    context={
    "titulo":titulo,
    'form':form,
    'accion':accion,
    }
    return render (request,"compras/compra/compra-crear.html", context )

def compra_detalle(request,compra_id):
    titulo="Compra"
    accion="Abrir"
    compra = get_object_or_404(Compra, id=compra_id)
    compras=CompraDetalle.objects.filter(compra=compra_id).annotate(
        subtotal=ExpressionWrapper(F('producto__precio_unitario_compra') * F('cantidad'), output_field= fields.DecimalField())
    )
    total= compras.aggregate(Sum('subtotal'))['subtotal__sum']


    if request.method=="POST":
        form= CompraDetalleForm(request.POST)
        if form.is_valid():
            producto_id= form.cleaned_data['producto'].id
            cantidad_nueva= form.cleaned_data['cantidad']

            detalle_existente= CompraDetalle.objects.filter(compra=compra, producto=producto_id).first()

            if detalle_existente:
                detalle_existente.cantidad= F('cantidad')+cantidad_nueva
                detalle_existente.save()
            else:
                compra_detalle = form.save(commit=False)
                compra_detalle.compra = compra
                compra_detalle.save()

            messages.success(request, '¡Se ha agregado el producto!')
            return redirect('compra_detalle', compra_id=compra.id)
        else:
            messages.error(request, f'¡Error al agregar producto')
    else:
        form=CompraDetalleForm()
    context={
    "titulo":titulo,
    "compras":compras,
    "compra":compra,
    'form':form,
    'accion':accion,
    'total': total,
    }
    return render (request,"compras/compra/compra-detalle.html", context )

def compra_eliminar(request, compra_id):
    detalles= CompraDetalle.objects.filter(compra=compra_id).first()
    compra= get_object_or_404(Compra, id=compra_id)

    if detalles:
        messages.warning(request, '¡No se puede eliminar una compra con productos registrados!')
    else:
        messages.success(request, '¡Se ha eliminado la compra!')
        compra.delete()
    return redirect("compras")





def compra_detalle_eliminar(request,compra_id,detalle_id):
    compra = get_object_or_404(Compra, id=compra_id)
    detalle = get_object_or_404(CompraDetalle, id=detalle_id,compra=compra)

    detalle.delete()
    messages.success(request, '¡Se ha eliminado el producto de esta compra!')
    return redirect("compra_detalle", compra_id=compra.id)


def compra_cerrar(request,compra_id):

    compra= get_object_or_404(Compra,id=compra_id)
    compra.estado= Compra.Estado.CERRADA
    compra.save()
    messages.success(request, '¡Se ha Cerrado esta compra!')

    return redirect("compras")