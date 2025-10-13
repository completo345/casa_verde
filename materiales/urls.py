from django.urls import path
from . import views

urlpatterns = [
   path('datos-terreno/', views.editar_datos_terreno, name='editar_datos_terreno'),
]


#solo espero que funcione 