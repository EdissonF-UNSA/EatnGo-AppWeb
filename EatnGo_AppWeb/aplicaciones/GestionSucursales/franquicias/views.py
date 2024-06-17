from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from .models import Franquicia
# from .forms import FranquiciaForm


class AdminFranquiciasView(TemplateView):
    template_name = 'gestionSucursales/ListaRegistroSucursales.html'
    # form_class = FranquiciaForm
    # success_url = '/admin_franquicias/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['franquicias'] = Franquicia.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if 'adicionar' in request.POST:
            return self.form_valid(self.get_form())
        # Maneja otros botones aquí (modificar, eliminar, etc.)
        return super().post(request, *args, **kwargs)
