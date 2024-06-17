from django.urls import path

from . import views

app_name = "franquicias_app"

urlpatterns = [
    path('listRegistroSucursales/', views.AdminFranquiciasView.as_view(), name='listRegistroSucursales'),

]