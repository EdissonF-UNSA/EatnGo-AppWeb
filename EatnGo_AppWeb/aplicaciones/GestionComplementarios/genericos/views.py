from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Region, Provincia, Distrito, Direccion
from .forms import RegionForm, ProvinciaForm, DistritoForm, DireccionForm

# Region Views
class RegionListView(ListView):
    model = Region
    template_name = 'GestionComplementarios/genericos/region_list.html'
    context_object_name = 'regiones'
    paginate_by = 5  # Número de elementos por página

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        regiones_list = Region.objects.all()
        paginator = Paginator(regiones_list, self.paginate_by)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        return context

class RegionCreateView(CreateView):
    model = Region
    form_class = RegionForm
    template_name = 'GestionComplementarios/genericos/region_form.html'
    success_url = reverse_lazy('genericos:region_list')  # Uso del espacio de nombres

class RegionUpdateView(UpdateView):
    model = Region
    form_class = RegionForm
    template_name = 'GestionComplementarios/genericos/region_form.html'
    success_url = reverse_lazy('genericos:region_list')  # Uso del espacio de nombres
    lookup_field = 'codigo'  # Utilizar el campo 'codigo' como identificador

class RegionDeleteView(DeleteView):
    model = Region
    template_name = 'GestionComplementarios/genericos/region_confirm_delete.html'
    success_url = reverse_lazy('genericos:region_list')  # Uso del espacio de nombres

# Provincia Views
class ProvinciaListView(ListView):
    model = Provincia
    template_name = 'GestionComplementarios/genericos/provincia_list.html'
    context_object_name = 'provincia'
    paginate_by = 5  # Número de elementos por página

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        provincias_list = Provincia.objects.all()
        paginator = Paginator(provincias_list, self.paginate_by)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        return context

# Vista para editar campos de modelo Provincia

class ProvinciaCreateView(CreateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'GestionComplementarios/genericos/provincia_form.html'
    success_url = reverse_lazy('genericos:provincia_list')  # Uso del espacio de nombres

class ProvinciaUpdateView(UpdateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'GestionComplementarios/genericos/provincia_form.html'
    success_url = reverse_lazy('genericos:provincia_list')  # Uso del espacio de nombres
    lookup_field = 'codigo'  # Utilizar el campo 'codigo' como identificador

class ProvinciaDeleteView(DeleteView):
    model = Provincia
    template_name = 'GestionComplementarios/genericos/provincia_confirm_delete.html'
    success_url = reverse_lazy('genericos:provincia_list')  # Uso del espacio de nombres