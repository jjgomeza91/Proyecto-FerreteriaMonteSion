from django.shortcuts import render, redirect
from ventas.models import Cliente
from ventas.forms import ClienteForm
from django.contrib import messages


# Create your views here.
def clientes(request):
    titulo="Clientes"
    clientes = Cliente.objects.all()
    context={
        "titulo": titulo,
        "clientes":clientes,
    }
    return render(request, "ventas/clientes/clientes.html", context)

def cliente_crear(request):
    titulo="Clientes"
    accion="Agregar"
    if request.method=="POST":
        form= ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            cliente=form.save()
            cliente.save()
            messages.success(request, f'¡El cliente se guardó de forma exitosa!')
            return redirect('clientes')
        else:
            messages.error(request, f'¡Error al agregar al Cliente!')
    else:
        form=ClienteForm()
    context={
    "titulo":titulo,
    'form':form,
    'accion':accion,
    }
    return render (request,"ventas/clientes/nuevocliente.html", context )