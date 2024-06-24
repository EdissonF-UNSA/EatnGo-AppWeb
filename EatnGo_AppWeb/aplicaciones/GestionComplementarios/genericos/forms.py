from django import forms
from .models import Region, Provincia, Distrito, Direccion

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['id', 'nombre', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # Si la instancia ya existe (es una actualización)
            self.fields['id'].widget.attrs['readonly'] = True
        else:  # Si es un nuevo registro (creación)
            self.fields['id'].widget.attrs.pop('readonly', None)

    def clean_id(self):
        id = self.cleaned_data['id']
        if self.instance.pk:  # Verificar si ya existe una instancia (es una actualización)
            existing_region = Region.objects.exclude(pk=self.instance.pk).filter(id=id)
        else:  # Es una creación de nuevo registro
            existing_region = Region.objects.filter(id=id)

        if existing_region.exists():
            raise forms.ValidationError("El ID ya está siendo utilizado por otra región.")

        return id

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = ['id', 'nombre', 'region', 'estado']

class DistritoForm(forms.ModelForm):
    class Meta:
        model = Distrito
        fields = ['id', 'nombre', 'provincia', 'estado']

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['provincia', 'distrito', 'informacion_adicional']