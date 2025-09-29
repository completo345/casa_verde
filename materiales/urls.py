from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='materiales'),
]


#por culpa de estas lineas de codigo casi mando a la mierda todo, en fin