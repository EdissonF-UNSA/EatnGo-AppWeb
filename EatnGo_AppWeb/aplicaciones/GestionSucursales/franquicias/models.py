from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    # Otros campos relevantes para empleados

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Franquicia(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    gerente = models.CharField(max_length=100) #Por Ahora solo nombre

    def __str__(self):
        return self.nombre
