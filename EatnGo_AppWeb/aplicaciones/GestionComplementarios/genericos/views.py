from django.shortcuts import render

# Create your views here.
# genericos/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Region, Provincia, Distrito, Direccion
from .forms import RegionForm, ProvinciaForm, DistritoForm, DireccionForm

# Region Views
class RegionListView(ListView):
    model = Region
    template_name = 'GestionComplementarios/genericos/region_list.html'
    context_object_name = 'regiones'

class RegionCreateView(CreateView):
    model = Region
    form_class = RegionForm
    template_name = 'GestionComplementarios/genericos/region_form.html'
    success_url = reverse_lazy('region_list')

class RegionUpdateView(UpdateView):
    model = Region
    form_class = RegionForm
    template_name = 'GestionComplementarios/genericos/region_form.html'
    success_url = reverse_lazy('region_list')

class RegionDeleteView(DeleteView):
    model = Region
    template_name = 'GestionComplementarios/genericos/region_confirm_delete.html'
    success_url = reverse_lazy('region_list')

# Repeat similarly for Provincia, Distrito, and Direccion
