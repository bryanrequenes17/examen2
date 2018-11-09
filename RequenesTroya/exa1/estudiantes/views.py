from django.shortcuts import render, redirect
from django.http import HttpResponse
from exa1.modelo.models import Estudiantes
from django.contrib.auth.decorators import login_required
from .forms import FormularioEstudiante
# Create your views here.


def principal(request):
    listaEstudiante = Estudiantes.objects.all().filter(estado=True).order_by('apellidos')
    context = {
            'lista': listaEstudiante,
    }
    return render(request, 'estudiantes/principal_estudiante.html', context)
    
def saludar(request):
    return HttpResponse('Hola')

def crear(request):
    formulario = FormularioEstudiante(request.POST)

    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            estudiante = Estudiantes()
            estudiante.cedula = datos.get('cedula')
            estudiante.nombres = datos.get('nombres')
            estudiante.edad = datos.get('edad') 
            estudiante.apellidos = datos.get('apellidos')
            estudiante.genero = datos.get('genero')
            estudiante.direccion = datos.get('direccion')
            estudiante.save()
            return redirect(principal)

    context={
        'f': formulario,
        'mensaje': 'Bienvenidos', 
    }
    return render(request, 'estudiantes/crear_estudiante.html', context)
