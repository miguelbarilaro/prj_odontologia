from django.shortcuts import render, redirect
from .models import Persona, Localidad
from .forms import PersonaForm, LocalidadForm
# Create your views here.

from django.shortcuts import render

def index(request, template_name="odontologia/index.html"):
    return render(request, template_name)


def personas_listar(request, template_name='odontologia/personas.html'):
    personas = Persona.objects.all()
    dato_personas = {'personas': personas}
    return render(request, template_name, dato_personas)

def localidades_listar(request, template_name='odontologia/localidades.html'):
    localidades = Localidad.objects.all()
    dato_localidades = {'localidades': localidades}
    return render(request, template_name, dato_localidades)

def nuevo_persona(request, template_name='odontologia/persona_form.html'):
    if request.method=='POST':
        form =PersonaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('personas')
        else:
            print(form.errors)
    else:
        form = PersonaForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def nuevo_localidad(request, template_name='odontologia/localidad_form.html'):
    if request.method=='POST':
        form = LocalidadForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('localidades')
        else:
            print(form.errors)
    else:
        form = LocalidadForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def modificar_persona(request, pk,template_name='odontologia/persona_form.html'):
    persona = Persona.objects.get(num_doc=pk)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save(commit=True)
        return redirect('personas')
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request, template_name, datos)

def modificar_localidad(request, pk, template_name='odontologia/localidad_form.html'):
    localidad = Localidad.objects.get(cp=pk)
    form = LocalidadForm(request.POST or None, instance=localidad)
    if form.is_valid():
        form.save(commit=True)
        return redirect('localidades')
    else:
        print(form.errors)
    datos = {'form': form}
    return render(request, template_name, datos)

def eliminar_persona(request, pk, template_name='odontologia/persona_confirmar_eliminacion.html'):
    persona = Persona.objects.get(num_doc=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('personas')
    else:
        return render(request, template_name, {'form':persona})

def eliminar_localidad(request, pk, template_name='odontologia/localidad_confirmar_eliminacion.html'):
    localidad = Localidad.objects.get(cp=pk)
    if request.method == 'POST':
        localidad.delete()
        return redirect('localidades')
    else:
        return render(request, template_name, {'form': localidad})