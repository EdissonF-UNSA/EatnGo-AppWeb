from django.db import models

class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    precio_articulo = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    precio_ingrediente = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    nombre_comercial = models.CharField(max_length=100, unique=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='recetas')
    ingredientes = models.ManyToManyField(Ingrediente, through='RecetaIngrediente')

    def __str__(self):
        return self.nombre_comercial

class RecetaIngrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('receta', 'ingrediente')

class Pizza(models.Model):
    articulo = models.OneToOneField(Articulo, on_delete=models.CASCADE, primary_key=True, related_name='pizza')
    tamanos = models.CharField(max_length=50)
    masa = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.articulo.nombre} - Pizza"

class Bocadillo(models.Model):
    articulo = models.OneToOneField(Articulo, on_delete=models.CASCADE, primary_key=True, related_name='bocadillo')
    tamanos = models.CharField(max_length=50)
    tipo_pan = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.articulo.nombre} - Bocadillo"

class Complemento(models.Model):
    articulo = models.OneToOneField(Articulo, on_delete=models.CASCADE, primary_key=True, related_name='complemento')
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.articulo.nombre} - Complemento"
