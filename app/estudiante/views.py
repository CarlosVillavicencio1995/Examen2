from django.shortcuts import render, redirect
from app.modelo.models import Usuario
from .forms import FormularioUsuario
# Create your views here.

def Principal(request):
    listaUsuarios = Usuario.objects.all().filter(estado=True)
    context = {
        'lista' : listaUsuarios
    }
    return render(request, 'principal_usuario.html', context)

def crear(request):
    formulario = FormularioUsuario(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            usuario = Usuario()
            usuario.cedula = datos.get('cedula')
            usuario.nombres = datos.get('nombres')
            usuario.apellidoPaterno = datos.get('apellidoPaterno')
            usuario.apellidoMaterno = datos.get('apellidoMaterno')
            usuario.Sexo = datos.get('Sexo')
            usuario.estado = datos.get('estado')
            usuario.save()
            return redirect(Principal)

    context = {
        'f': formulario,
        'mensaje': '',
    }
    return render(request, 'crear_usuario.html', context)

def modificar(request):
    dni = request.GET['cedula']
    usuario = Usuario.objects.get(cedula = dni)
    formulario = FormularioUsuario(request.POST, instance=usuario)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            usuario.cedula = datos.get('cedula')
            usuario.nombres = datos.get('nombres')
            usuario.apellidoPaterno = datos.get('apellidoPaterno')
            usuario.apellidoMaterno = datos.get('apellidoMaterno')
            usuario.Sexo = datos.get('Sexo')
            usuario.estado = datos.get('estado')
            usuario.save()
            return redirect(Principal)
    else:
        formulario = FormularioUsuario(instance=usuario)

    context = {
        'f': formulario,
    }
    return render(request, 'crear_usuario.html', context)

def eliminar(request):
    dni = request.GET['cedula']
    usuario = Usuario.objects.get(cedula=dni)
    usuario.estado = False
    usuario.save()
    return redirect(Principal)
