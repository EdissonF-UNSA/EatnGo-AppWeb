from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
    CreateView
)


# Create your views here.
class HomePageView(TemplateView):
    template_name = "GestionHomeWeb/homeWeb/index.html"


class PanelPageView(LoginRequiredMixin, TemplateView):
    template_name = "GestionHomeWeb/homeWeb/panel.html"
    # login_url = 'gestionUsuarios_app:user-login'
