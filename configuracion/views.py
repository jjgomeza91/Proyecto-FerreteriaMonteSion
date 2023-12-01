from django.shortcuts import render, redirect
from configuracion.models import Usuario
from configuracion.forms import UsuarioForm, UsuarioEditarForm
from PIL import Image
from django.contrib import messages

# Create your views here.
def usuarios(request):
    titulo="Usuarios"
    usuarios = Usuario.objects.all()
    context={
        "titulo": titulo,
        "usuarios":usuarios,
    }
    return render(request, "configuracion/usuarios/usuarios.html", context)

def usuario_crear(request):
    titulo="Usuarios"
    accion="Agregar"
    if request.method=="POST":
        form= UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            usuario=form.save()
            if usuario.imagen:
                img=Image.open(usuario.imagen.path)
                img=img.resize((500,500))
                img.save(usuario.imagen.path)
            usuario.save()
            messages.success(request, f'¡El usuario se guardó de forma exitosa!')
            return redirect('usuarios')
        else:
            messages.error(request, f'¡Error al agregar al Usuario!')
    else:
        form=UsuarioForm()
    context={
    "titulo":titulo,
    'form':form,
    'accion':accion,
    }
    return render (request,"configuracion/usuarios/nuevousuario.html", context )

def usuario_eliminar(request,pk):
    usuario=Usuario.objects.filter(id=pk)
    usuario.update(estado=False)
    ## Agregar mensaje de texto
    return redirect ('usuarios')

def usuario_editar(request,pk):
    usuario= Usuario.objects.get(id=pk)
    usuarios= Usuario.objects.all()
    accion="Editar"

    nombre=f"{usuario.primer_nombre} {usuario.primer_apellido}"
    titulo=f"Usuario {nombre}"


    if request.method=="POST":
        form= UsuarioEditarForm(request.POST,request.FILES,instance=usuario) 
        if form.is_valid():
            usuario= form.save()
            if usuario.imagen:
                img = Image.open(usuario.imagen.path)
                img= img.resize((500,500))
                img.save(usuario.imagen.path)
            usuario.save()
            messages.success(request, f'¡{nombre} se editó de forma exitosa!')
            return redirect("usuarios")
        else:
            messages.error(request, f'¡Error al editar a {nombre}!')
    else:
        form=UsuarioEditarForm(instance=usuario)

    context={
        "titulo":titulo,
        "usuarios":usuarios,
        "form":form,
        "accion":accion,
    }
    return render(request,"configuracion/usuarios/nuevousuario.html", context)
