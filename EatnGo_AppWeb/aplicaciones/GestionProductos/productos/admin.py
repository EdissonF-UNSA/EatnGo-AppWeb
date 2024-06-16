from django.contrib import admin


from .models import Articulo, Ingrediente, Receta, Pizza, Bocadillo, Complemento
# Register your models here.
admin.site.register(Articulo)
admin.site.register(Ingrediente)
admin.site.register(Receta)
admin.site.register(Pizza)
admin.site.register(Bocadillo)
admin.site.register(Complemento)