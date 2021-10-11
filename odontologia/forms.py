from django import forms
from dal import autocomplete
from django.forms import ModelForm
from .models import Localidad, Persona, Profesional,\
    Prestacion, PiezaDental, Paciente, Consulta,\
    Establecimiento, FichaMedica, ObraSocial, Usuario, Turno, \
    FichaMedicaConsulta, Calendario, CalendarioTurno
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input'}),
                   'cp': forms.TextInput(attrs={'class': 'form-control input'})}


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input',
                                                    'text-transform': 'capitalize',
                                                    'placeholder': 'Nombre del paciente'}),
                   'apellido': forms.TextInput(attrs={'class': 'form-control input',
                                                      'text-transform': 'capitalize'}),
                   'num_doc': forms.TextInput(attrs={'type': 'number',
                                                     'class': 'form-control input'}),
                   'num_cuit': forms.TextInput(attrs={'type': 'number',
                                                     'class': 'form-control input'}),
                   'fecha_nac': DateInput(format='%Y-%m-%d', attrs={'class': 'form-control input-sm'}),
                   'telefono': forms.TextInput(attrs={'class': 'form-control input'}),
                   'email': forms.TextInput(attrs={'class': ' form-control input'}),
                   'direccion': forms.TextInput(attrs={'class': ' form-control input'}),
                   'localidad': forms.Select(attrs={'class': ' form-control input'}),
                   }


class ProfesionalForm(ModelForm):
    class Meta:
        model = Profesional
        fields = '__all__'
        widgets = {'profesional': forms.Select(attrs={'class': 'form-control input'}),
                   'matricula': forms.TextInput(attrs={'type': 'number',
                                                       'class': 'form-control input'}),
                   'especialidad': forms.TextInput(attrs={'class': 'form-control input'})
                   }


class PrestacionForm(ModelForm):
    class Meta:
        model = Prestacion
        fields = '__all__'

class PiezaDentalForm(ModelForm):
    class Meta:
        model = PiezaDental
        fields = '__all__'


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {'persona': forms.Select(attrs={'class': 'form-control input'}),
                   'numeroHC': forms.TextInput(attrs={'class': 'form-control input'}),
                   'obrasocial': forms.Select(attrs={'class': 'form-control input'}),
                   'numeroOS': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input'}),
                   'titularOS': forms.NullBooleanSelect(attrs={'class': 'form-control input'})
                   }


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'


class EstablecimientoForm(ModelForm):
    class Meta:
        model = Establecimiento
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input'}),
                   'id': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input'}),
                   'direccion': forms.TextInput(attrs={'class': 'form-control input'}),
                   'localidad': forms.Select(attrs={'class': 'form-control input'}),
                   'telefono': forms.TextInput(attrs={'class': 'form-control input'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control input'}),
                   'web': forms.URLInput(attrs={'class': 'form-control input'})
                   }


class FichaMedicaForm(ModelForm):
    class Meta:
        model =FichaMedica
        fields = '__all__'


class FichaMedicaConsultaForm(ModelForm):
    class Meta:
        model = FichaMedicaConsulta
        fields = '__all__'


class ObraSocialForm(ModelForm):
    class Meta:
        model = ObraSocial
        fields = '__all__'
        widgets = {'nombreOS': forms.TextInput(attrs={'class': 'form-control input'}),
                   'cuit': forms.TextInput(attrs={'class': 'form-control input'}),
                   'direccion': forms.TextInput(attrs={'class': 'form-control input'}),
                   'disponible': forms.NullBooleanSelect(attrs={'class': 'form-control input'})
                   }


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {'persona': forms.Select(attrs={'class': 'form-control input'}),
                   'nombre_usuario': forms.TextInput(attrs={'class': 'form-control input'}),
                   'contraseña': forms.PasswordInput(attrs={'class': 'form-control input'})
                   }


class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'


class CalendarioForm(ModelForm):
    class Meta:
        model = Calendario
        fields = '__all__'


class CalendarioTurnoForm(ModelForm):
    class Meta:
        model = CalendarioTurno
        fields = '__all__'

