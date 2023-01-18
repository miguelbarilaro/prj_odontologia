from django.contrib import admin
from .models import *

my_models = [Localidad, Persona]
# Register your models here.

admin.site.register(my_models)