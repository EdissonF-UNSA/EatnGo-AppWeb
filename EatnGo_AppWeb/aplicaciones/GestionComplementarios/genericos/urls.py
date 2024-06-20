from django.urls import path
from . import views

app_name = 'genericos'  # Define el nombre de la aplicación

urlpatterns = [
    path('regiones/', views.RegionListView.as_view(), name='region_list'),
    path('regiones/nueva/', views.RegionCreateView.as_view(), name='region_create'),
    path('regiones/<str:pk>/editar/', views.RegionUpdateView.as_view(), name='region_update'),
    path('regiones/<str:pk>/eliminar/', views.RegionDeleteView.as_view(), name='region_delete'),
    path('regiones/<str:pk>/activar/', views.RegionActivateView, name='region_activate'),
    path('regiones/<str:pk>/desactivar/', views.RegionDeactivateView, name='region_deactivate'),

    # Otros paths para Provincia, Distrito, y Direccion
]
