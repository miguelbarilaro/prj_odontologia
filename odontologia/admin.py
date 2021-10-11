from django.contrib import admin
from .models import Localidad, Persona, Profesional, \
    Usuario, ObraSocial, Paciente, Consulta, FichaMedicaConsulta, \
    FichaMedica, Calendario, CalendarioTurno, PiezaDental, \
    Prestacion, Establecimiento, Turno


# Register your models here.
my_models = [Persona, Profesional, Paciente, Consulta,
             ObraSocial, Localidad, Usuario, FichaMedica,
             FichaMedicaConsulta, Calendario, CalendarioTurno,
             PiezaDental, Prestacion, Establecimiento, Turno]

admin.site.register(my_models)
