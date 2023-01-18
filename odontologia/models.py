from dal import autocomplete
from django.db import models
from datetime import datetime
# Create your models here.

DIA_CHOICE = (
    ('L', "Lunes"),
    ('M', "Martes"),
    ('X', "Miercoles"),
    ('J', "Jueves"),
    ('V', "Viernes"),
    ('S', "Sábado"),
    ('D', "Domingo")
)



class Localidad(models.Model):
    nombre = models.CharField("Localidad", max_length=50)
    cp = models.IntegerField("Código postal")

    class Meta:
        verbose_name_plural = "localidades"
    def __str__(self):
        return '%s - %s' % (self.cp, self.nombre)

class Persona(models.Model):
    num_doc = models.IntegerField("N° de documento", primary_key=True)
    nombre = models.CharField("Nombre/s", max_length=100)
    apellido = models.CharField("Apellido/s", max_length=100)
    num_cuit = models.IntegerField("N° de cuil/cuit", null=True, blank=True)
    fecha_nac = models.DateField("Fecha de nacimiento", default=datetime.now)
    telefono = models.IntegerField("N° de telefono")
    email = models.EmailField("Correo electronico", null=True, blank=True)
    direccion = models.CharField("Dirección", max_length=120)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, related_name="persona_localidad")

    class Meta:
        ordering = ["apellido", "nombre"]
        #Poder ordenar poner las entradas que deseemos

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)

'class PersonaAutocomplete(autocomplete.Select2QuerySetView):'


class Profesional(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)

class Calendario(models.Model):
    dia = models.CharField("Día de la semana", max_length=1, choices=DIA_CHOICE, default='L')
    hora = models.DateTimeField()