from django.urls import path
from . import views

app_name = 'genericos'  # Define el nombre de la aplicación

urlpatterns = [
    path('regiones/', views.RegionListView.as_view(), name='region_list'),
    path('regiones/nueva/', views.RegionCreateView.as_view(), name='region_create'),
    path('regiones/<str:pk>/editar/', views.RegionUpdateView.as_view(), name='region_update'),
    path('regiones/<str:pk>/eliminar/', views.RegionDeleteView.as_view(), name='region_delete'),
    # Provincias
    path('provincias/', views.ProvinciaListView.as_view(), name='provincia_list'),
    path('provincias/nueva/', views.ProvinciaCreateView.as_view(), name='provincia_create'),
    path('provincias/<str:pk>/editar/', views.ProvinciaUpdateView.as_view(), name='provincia_update'),
    path('provincias/<str:pk>/eliminar/', views.ProvinciaDeleteView.as_view(), name='provincia_delete'),
    # Distritos
    path('distritos/', views.DistritoListView.as_view(), name='distrito_list'),
    path('distritos/nueva/', views.DistritoCreateView.as_view(), name='distrito_create'),
    path('distritos/<str:pk>/editar/', views.DistritoUpdateView.as_view(), name='distrito_update'),
    path('distritos/<str:pk>/eliminar/', views.DistritoDeleteView.as_view(), name='distrito_delete'),
    # Estado Civil
    path('estadosciviles/', views.EstadoCivilListView.as_view(), name='estadocivil_list'),
    path('estadosciviles/nueva/', views.EstadoCivilCreateView.as_view(), name='estadocivil_create'),
    path('estadosciviles/<str:pk>/editar/', views.EstadoCivilUpdateView.as_view(), name='estadocivil_update'),
    path('estadosciviles/<str:pk>/eliminar/', views.EstadoCivilDeleteView.as_view(), name='estadocivil_delete'),
]
