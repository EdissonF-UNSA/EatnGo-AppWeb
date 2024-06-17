# genericos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('regiones/', views.RegionListView.as_view(), name='region_list'),
    path('regiones/nueva/', views.RegionCreateView.as_view(), name='region_create'),
    path('regiones/<int:pk>/editar/', views.RegionUpdateView.as_view(), name='region_update'),
    path('regiones/<int:pk>/eliminar/', views.RegionDeleteView.as_view(), name='region_delete'),
    # Repeat similarly for Provincia, Distrito, and Direccion
]
