from django.urls import path
from . import views

urlpatterns = [
    path("", views.elegir_provincia, name="materiales_index"),
    path("provincia/", views.elegir_provincia, name="elegir_provincia"),
    path("mis-datos/", views.datos_terreno, name="datos_terreno"),
]


#solo espero que funcione