# genericos/forms.py

from django import forms
from .models import Region, Provincia, Distrito, Direccion

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['nombre']

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = ['nombre', 'region']

class DistritoForm(forms.ModelForm):
    class Meta:
        model = Distrito
        fields = ['nombre', 'provincia']

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['provincia', 'distrito', 'informacion_adicional']
