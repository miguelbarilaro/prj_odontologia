from django.db import models
from datetime import datetime


# Create your models here.

DIA_CHIOCE = (
    ('L', 'Lunes'),
    ('M', 'Martes'),
    ('I', 'Miercoles'),
    ('J', 'Juves'),
    ('V', 'Viernes'),
    ('S', 'Sabado'),
    ('D', 'Domingo')
)




class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    cp = models.CharField("Código Postal", max_length=10)

    class Meta:
        verbose_name_plural = 'localidades'

    def __str__(self):
        return '%s - %s' % (self.nombre, self.cp)



class Persona(models.Model):
    num_doc = models.CharField("Nº de documento", max_length=20, primary_key=True)
    nombre = models.CharField("Nombre/s", max_length=150)
    apellido = models.CharField("Apellido/s", max_length=150)
    num_cuit = models.CharField("Nº de CUIT/CUIL", max_length=20, null=True, blank=True)
    fecha_nac = models.DateField("Fecha de Nacimiento", default=datetime.now)
    telefono = models.CharField("Numero de telefono", max_length=20, null=True, blank=True)
    email = models.EmailField("E-mail", null=True, blank=True)
    direccion = models.CharField("Dirección", max_length=120, )
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, related_name="persona_localidad")

    class Meta:
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)



class Usuario(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name="usuario_persona")
    nombre_usuario = models.CharField("Nombre de Usuario", max_length=100)
    contraseña = models.CharField("Contraseña de Usuario", max_length=100)

    # class Meta:
    #     ordering = ["nombre", "persona"]

    def __str__(self):
        return '%s, %s, %s' % (self.nombre_usuario, self.persona.apellido, self.persona.nombre)



class ObraSocial(models.Model):
    nombreOS = models.CharField("Nombre - Obra Social", max_length=100)
    cuit = models.CharField("CUIT", max_length=20, primary_key=True)
    direccion = models.CharField(max_length=100)
    disponible = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.nombreOS



class Paciente(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name="paciente_persona")
    numeroHC = models.CharField("Hoja Clínica", max_length=20, primary_key=True)
    obrasocial = models.ForeignKey(ObraSocial, on_delete=models.PROTECT, related_name="paciente_obrasocial")
    numeroOS = models.CharField("Número de la Obra Social", max_length=50)
    titularOS = models.BooleanField("¿Es titular de la obra social?", default=False)

    def __str__(self):
        return '%s, %s' % (self.persona, self.numeroOS)



class Profesional(models.Model):
    profesional = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name="profesional_persona")
    matricula = models.CharField(max_length=100, primary_key=True)
    especialidad = models.CharField(max_length=200)

    def __str__(self):
        return '%s, %s' % (self.profesional, self.matricula)



class PiezaDental(models.Model):
    nombre = models.CharField("Pieza Dental", max_length=50)

    def __str__(self):
        return self.nombre



class Prestacion(models.Model):
    nombre = models.CharField("Prestación", max_length=200)
    descripcion = models.CharField(max_length=300)
    pieza_dental = models.ForeignKey(PiezaDental, on_delete=models.PROTECT, related_name="pieza_dental_prestacion")

    def __str__(self):
        return self.nombre



class Consulta(models.Model):
    medico = models.ForeignKey(Profesional, on_delete=models.PROTECT, related_name="medico_consulta")
    prestacion = models.ForeignKey(Prestacion, on_delete=models.PROTECT, related_name="prestacion_consulta")
    fecha = models.DateField(default=datetime.now)
    receta = models.CharField(max_length=500)
    obs = models.CharField("Observaciones", max_length=500)

    def __str__(self):
        return '%s, %s' % (self.medico, self.prestacion)



class FichaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name="ficha_paciente")
    fecha_alta = models.DateField("Alta Médica", default=datetime.now)
    tipo_sangre = models.CharField("Tipo de Sangre", max_length=10)
    antecedentes = models.CharField(max_length=500)

    def __str__(self):
        return self.paciente



class FichaMedicaConsulta(models.Model):
    ficha_medica = models.ForeignKey(FichaMedica, on_delete=models.PROTECT, related_name="FichaMedica_Consulta_FichaMedica")
    consulta = models.ForeignKey(Consulta, on_delete=models.PROTECT, related_name="FichaMedica_Consulta_Consulta")

    def __str__(self):
        return '%s, %s' % (self.ficha_medica, self.consulta)



class Establecimiento(models.Model):
    nombre = models.CharField(max_length=100)
    id = models.CharField("Identificador", max_length=50, primary_key=True)
    direccion = models.CharField(max_length=100)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, related_name="establecimiento_localidad")
    telefono = models.CharField(max_length=50)
    email = models.EmailField("E-mail")
    web = models.URLField("Sitio Web", max_length=200)

    def __str__(self):
        return self.nombre



class Turno(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.PROTECT, related_name="turno_establecimiento")
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name="turno_paciente")
    medico = models.ForeignKey(Profesional, on_delete=models.PROTECT, related_name="turno_medico")
    consultorio = models.CharField(max_length=5)
    fecha = models.DateField("Fecha de la consulta", default=datetime.now)

    class Meta:
        ordering = ["paciente", "medico", "consultorio", "fecha"]

    def __str__(self):
        return self.paciente



class Calendario(models.Model):
    dia = models.CharField("Dia de la semana", max_length=1, choices=DIA_CHIOCE, default='L')
    hora = models.DateTimeField

    def __str__(self):
        return '%s, %s' % (self.dia, self.hora)




class CalendarioTurno(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.PROTECT, related_name="Calendario_turno_profesional")
    dia_hora = models.ForeignKey(Calendario, on_delete=models.PROTECT, related_name="turno_dia_hora")

    def __str__(self):
        return '%s, %s' % (self.profesional, self.dia_hora)
