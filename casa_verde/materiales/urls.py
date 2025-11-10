from django.urls import path
from . import views

urlpatterns = [
    path('datos-terreno/', views.editar_datos_terreno, name='editar_datos_terreno'),
    path('', views.lista_materiales, name='lista_materiales'),  # esta será la raíz /materiales/
]
