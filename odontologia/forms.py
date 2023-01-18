from django import forms
from django.forms import ModelForm
from .models import Localidad, Persona

class DateInput(forms.DateInput):
    input_type = 'date'


class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__' # Para definir todos los campos de un formulario

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class':'form-control input', 'text-transform':'capitalize', 'placeholder':'Nombre paciente'}),
                   'apellido': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize', 'placeholder':'Apellido paciente'}),
                   'num_doc': forms.TextInput(attrs={'type':'number', 'class': 'form-control input', 'placeholder':'N° de documento'}),
                   'num_cuit': forms.TextInput(attrs={'type':'number', 'class': 'form-control input', 'placeholder':'N° de cuil/cuit'}),
                   'fecha_nac': DateInput(format='%Y-%m-%d', attrs={'class':'form-control input-sm'}),
                   'telefono': forms.TextInput(attrs={'type':'number', 'class': 'form-control input', 'placeholder':'N° de telefono'}),
                   'email': forms.TextInput(attrs={'class': 'form-control input', 'placeholder':'E-mail'}),
                   'direccion': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize', 'placeholder':'Dirección'}),
                   'localidad': forms.Select(attrs={'class':'form-control input'})
                    }