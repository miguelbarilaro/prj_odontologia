from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('personas', views.personas_listar, name="personas"),
    path("nuevo_persona", views.nuevo_persona, name="nuevo_persona"),
    path("modificar_persona/<int:pk>", views.modificar_persona, name="modificar_persona"),
    path("eliminar_persona/<int:pk>", views.eliminar_persona, name="eliminar_persona"),
    path('localidades', views.localidades_listar, name="localidades"),
    path("nuevo_localidad", views.nuevo_localidad, name="nuevo_localidad"),
    path("modificar_localidad/<int:pk>", views.modificar_localidad, name="modificar_localidad"),
    path("eliminar_localidad/<int:pk>", views.eliminar_localidad, name="eliminar_localidad")
]