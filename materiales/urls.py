from django.urls import path
from . import views

urlpatterns = [
    path("provincia/", views.elegir_provincia, name="elegir_provincia"),
    path("mis-datos/", views.datos_terreno, name="datos_terreno"),
]


#solo espero que funcione 