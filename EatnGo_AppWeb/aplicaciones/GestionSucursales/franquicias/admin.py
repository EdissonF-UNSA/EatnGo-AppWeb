from django.contrib import admin


# Importaciones locales
from .models import Franquicia, Empleado

admin.site.register(Franquicia)
admin.site.register(Empleado)

