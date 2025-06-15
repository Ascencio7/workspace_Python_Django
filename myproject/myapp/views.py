from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Persona
from django.contrib.auth.decorators import login_required
from .forms import PersonaForm
# Create your views here.



@login_required(login_url = 'accounts/login/')
def inicio(request):
    return render(request, 'index.html')


def hola(request):
   return HttpResponse("Hola soy Jonathan Vladimir Ascencio Ramos")

def mostrarValor(request, value):
  return HttpResponse(f'Este es el valor: {value}')

def mostrarTexto(request, value):
    return HttpResponse(f'Este es el valor: {value}')

"""Este es el conjunto de nuevas vistas a agregar"""

def personaCrear(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personas-url')
        
    form = PersonaForm()
    return render(request, 'crear.html', {'form': form})

def personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas.html', {'personas': personas})


def personaActualizar(request, id):
    persona = Persona.objects.get(pk=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('personas-url')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'crear.html', {'form': form})

def personaEditar(request, id):
    form = Persona.objects.get(id=id)
    return render(request, 'editar.html', {'form':form})

def personaBorrar(request, id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    return redirect('personas-url')
