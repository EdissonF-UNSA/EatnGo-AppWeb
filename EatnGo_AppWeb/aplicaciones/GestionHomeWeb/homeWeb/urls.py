from django.urls import path

from . import views

app_name = "homeWeb_app"

urlpatterns = [
    path('index', views.HomePageView.as_view(), name='index'),
    path('panel/', views.PanelPageView.as_view(), name='panel'),

]