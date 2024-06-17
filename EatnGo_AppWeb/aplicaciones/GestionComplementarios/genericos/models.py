# genericos/models.py

from django.db import models

class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} ({self.region.nombre})'

class Distrito(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} ({self.provincia.nombre})'

class Direccion(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    informacion_adicional = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.distrito.nombre}, {self.provincia.nombre}'
