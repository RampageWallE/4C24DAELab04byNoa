from django.urls import path
from . import views

urlpatterns = [
    path('entradas/', views.lista_entradas, name='lista_entradas'),
    path('entradas/<str:nombre1>/',views.lista_entradas_autor, name='lista_entradas_autor'),
]
