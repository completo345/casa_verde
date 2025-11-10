from django import forms
from .models import DatosTerreno

class DatosTerrenoForm(forms.ModelForm):
    class Meta:
        model = DatosTerreno
        fields = ['provincia', 'comuna', 'orientacion_terreno', 'pendiente_terreno', 'exposicion_solar', 'velocidad_viento', 'tipo_suelo']
        labels = {
            'provincia': 'Provincia',
            'comuna': 'Comuna',
            'orientacion_terreno': 'Orientación del Terreno',
            'pendiente_terreno': 'Pendiente del Terreno',
            'exposicion_solar': 'Exposición Solar',
            'velocidad_viento': 'Velocidad del Viento',
            'tipo_suelo': 'Tipo de Suelo',
        }