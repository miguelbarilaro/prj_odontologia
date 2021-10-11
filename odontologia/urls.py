from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("personas", views.personas_listar, name="personas"),
    path("localidades", views.localidades_listar, name="localidades"),
    path("profesionales", views.profesionales_listar, name="profesionales"),
    path("usuarios", views.usuarios_listar, name="usuarios"),
    path("obrasocial", views.obrasocial_listar, name="obrasocial"),
    path("pacientes", views.pacientes_listar, name="pacientes"),
    path("establecimientos", views.establecimientos_listar, name="establecimientos"),
    path("nuevo_persona", views.nuevo_persona, name="nuevo_persona"),
    path("nuevo_profesional", views.nuevo_profesional, name="nuevo_profesional"),
    path("nuevo_paciente", views.nuevo_paciente, name="nuevo_paciente"),
    path("nuevo_obrasocial", views.nuevo_obrasocial, name="nuevo_obrasocial"),
    path("nuevo_localidad", views.nuevo_localidad, name="nuevo_localidad"),
    path("nuevo_usuario", views.nuevo_usuario, name="nuevo_usuario"),
    path("nuevo_establecimiento", views.nuevo_establecimiento, name="nuevo_establecimiento"),
    path("modificar_persona/<int:pk>", views.modificar_persona, name="modificar_persona"),
    path("modificar_profesional/<int:pk>", views.modificar_profesional, name="modificar_profesional"),
    path("modificar_paciente/<int:pk>", views.modificar_paciente, name="modificar_paciente"),
    path("modificar_usuario/<int:pk>", views.modificar_usuario, name="modificar_usuario"),
    path("modificar_establecimiento/<int:pk>", views.modificar_establecimiento, name="modificar_establecimiento"),
    path("modificar_obrasocial/<int:pk>", views.modificar_obrasocial, name="modificar_obrasocial"),
    path("eliminar_persona/<int:pk>", views.eliminar_persona, name="eliminar_persona"),
    path("eliminar_profesional/<int:pk>", views.eliminar_profesional, name="eliminar_profesional"),
    path("eliminar_paciente/<int:pk>", views.eliminar_paciente, name="eliminar_paciente"),
    path("eliminar_establecimiento/<int:pk>", views.eliminar_establecimiento, name="eliminar_establecimiento"),
    path("eliminar_obrasocial/<int:pk>", views.eliminar_obrasocial, name="eliminar_obrasocial")
]
