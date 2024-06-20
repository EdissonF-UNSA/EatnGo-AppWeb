from django.db import models

class Region(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    nombre = models.CharField(unique=False, max_length=30)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} ({self.region.nombre})'

class Distrito(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} ({self.provincia.nombre})'

class Direccion(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    informacion_adicional = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.distrito.nombre}, {self.provincia.nombre}'
