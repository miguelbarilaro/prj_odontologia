from django.shortcuts import render, redirect
from .models import Persona, Localidad, Profesional, \
    Usuario, ObraSocial, Paciente, Establecimiento
from .forms import PersonaForm, ProfesionalForm, PacienteForm, \
    ObraSocialForm, LocalidadForm, UsuarioForm, EstablecimientoForm
from dal import autocomplete
# Create your views here.

def index(request, template_name='odontologia/index.html'):
    return render(request, template_name)




def personas_listar(request, template_name='odontologia/personas.html'):
    personas = Persona.objects.all()
    dato_personas = {"personas": personas}
    return render(request, template_name, dato_personas)

def localidades_listar(request, template_name='odontologia/localidades.html'):
    localidades = Localidad.objects.all()
    dato_localidades = {"localidades": localidades}
    return render(request, template_name, dato_localidades)

def profesionales_listar(request, template_name='odontologia/profesionales.html'):
    profesionales = Profesional.objects.all()
    dato_profesionales = {"profesionales": profesionales}
    return render(request, template_name, dato_profesionales)

def usuarios_listar(request, template_name='odontologia/usuarios.html'):
    usuarios = Usuario.objects.all()
    dato_usuarios = {"usuarios": usuarios}
    return render(request, template_name, dato_usuarios)

def obrasocial_listar(request, template_name='odontologia/obrasocial.html'):
    obrassociales = ObraSocial.objects.all()
    dato_obrasociales = {"obrassociales": obrassociales}
    return render(request, template_name, dato_obrasociales)

def pacientes_listar(request, template_name='odontologia/pacientes.html'):
    pacientes = Paciente.objects.all()
    dato_pacientes = {"pacientes": pacientes}
    return render(request, template_name, dato_pacientes)

def establecimientos_listar(request, template_name='odontologia/establecimientos.html'):
    establecimientos = Establecimiento.objects.all()
    dato_establecimientos = {"establecimientos": establecimientos}
    return render(request, template_name, dato_establecimientos)




def nuevo_persona(request, template_name='odontologia/persona_form.html'):
    if request.method=='POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('personas')
    else:
        form = PersonaForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def nuevo_profesional(request, template_name='odontologia/profesional_form.html'):
    if request.method=='POST':
        form = ProfesionalForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profesionales')
    else:
        form = ProfesionalForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def nuevo_paciente(request,template_name='odontologia/paciente_form.html'):
    if request.method=='POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('pacientes')
    else:
        form = PacienteForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def nuevo_obrasocial(request, template_name='odontologia/obrasocial_form.html'):
    if request.method=='POST':
        form = ObraSocialForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('obrasocial')
    else:
        form = ObraSocialForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def nuevo_localidad(request, template_name='odontologia/localidades_form.html'):
    if request.method=='POST':
        form = LocalidadForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('localidades')
    else:
        form = LocalidadForm()
    dato = {'form': form}
    return render(request, template_name, dato)

def nuevo_usuario(request, template_name='odontologia/usuario_form.html'):
    if request.method=='POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    dato = {'form': form}
    return render(request, template_name, dato)

def nuevo_establecimiento(request, template_name='odontologia/establecimiento_form.html'):
    if request.method=='POST':
        form = EstablecimientoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('establecimientos')
    else:
        form = EstablecimientoForm()
    dato = {'form': form}
    return render(request, template_name, dato)






def modificar_persona(request, pk, template_name='odontologia/persona_form.html'):
    persona = Persona.objects.get(num_doc=pk)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save(commit=True)
        return redirect('personas')
    else:
        print(form.errors)
    dato = {'form': form}
    return render(request, template_name, dato)

def modificar_profesional(request, pk, template_name='odontologia/profesional_form.html'):
    profesional = Profesional.objects.get(profesional=pk)
    form = ProfesionalForm(request.POST or None, instance=profesional)
    if form.is_valid():
        form.save(commit=True)
        return redirect('profesionales')
    else:
        print(form.errors)
    dato = {'form': form}
    return render(request, template_name, dato)

def modificar_paciente(request, pk, template_name='odontologia/paciente_form.html'):
    paciente = Paciente.objects.get(persona=pk)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save(commit=True)
        return redirect('pacientes')
    else:
        print(form.errors)
    dato = {'form': form}
    return render(request, template_name, dato)

def modificar_usuario(request, pk, template_name='odontologia/usuario_form.html'):
    usuario = Usuario.objects.get(persona=pk)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save(commit=True)
        return redirect('usuarios')
    else:
        print(form.errors)
    dato = {'form': form}
    return render(request, template_name, dato)

def modificar_establecimiento(request, pk, template_name='odontologia/establecimiento_form.html'):
    establecimiento = Establecimiento.objects.get(id=pk)
    form = EstablecimientoForm(request.POST or None, instance=establecimiento)
    if form.is_valid():
        form.save(commit=True)
        return redirect('establecimientos')
    else:
        print(form.errors)
        dato = {'form': form}
        return render(request, template_name, dato)

def modificar_obrasocial(request, pk, template_name='odontologia/obrasocial_form.html'):
    obrasocial = ObraSocial.objects.get(cuit=pk)
    form = ObraSocialForm(request.POST or None, instance=obrasocial)
    if form.is_valid():
        form.save(commit=True)
        return redirect('obrasocial')
    else:
        print(form.errors)
        dato = {'form': form}
        return render(request, template_name, dato)







def eliminar_persona(request, pk, template_name='odontologia/persona_confirmar_eliminacion.html'):
    persona = Persona.objects.get(num_doc=pk)
    if request.method=='POST':
        persona.delete()
        return redirect('personas')
    else:
        return render(request, template_name, {'form': persona})

def eliminar_profesional(request, pk, template_name='odontologia/profesional_confirmar_eliminacion.html'):
    profesional = Profesional.objects.get(profesional=pk)
    if request.method=='POST':
        profesional.delete()
        return redirect('profesionales')
    else:
        return render(request, template_name, {'form': profesional})

def eliminar_paciente(request, pk, template_name='odontologia/paciente_confirmar_eliminacion.html'):
    paciente = Paciente.objects.get(persona=pk)
    if request.method=='POST':
        paciente.delete()
        return redirect('pacientes')
    else:
        return render(request, template_name, {'form': paciente})

def eliminar_establecimiento(request, pk, template_name='odontologia/establecimiento_confirmar_eliminacion.html'):
    establecimiento = Establecimiento.objects.get(id=pk)
    if request.method=='POST':
        establecimiento.delete()
        return redirect('establecimientos')
    else:
        return render(request, template_name, {'form': establecimiento})

def eliminar_obrasocial(request, pk, template_name='odontologia/obrasocial_confirmar_eliminacion.html'):
    obrasocial = ObraSocial.objects.get(cuit=pk)
    if request.method=='POST':
        obrasocial.delete()
        return redirect('obrasocial')
    else:
        return render(request, template_name, {'form': obrasocial})
