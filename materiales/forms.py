from django import forms
from materiales.models import ProvinciaDatos, Material

PROVINCIAS_VALPARAISO = [
    ("Valparaíso", (-33.0472, -71.6127)),
    ("Marga Marga", (-33.0458, -71.4496)),
    ("San Felipe de Aconcagua", (-32.7490, -70.7250)),
    ("Los Andes", (-32.8332, -70.5980)),
    ("Quillota", (-32.8800, -71.2480)),
    ("Petorca", (-32.2500, -70.9300)),
    ("Isla de Pascua", (-27.1127, -109.3497)),
]

class ProvinciaForm(forms.Form):
    provincia = forms.ChoiceField(choices=[(p[0], p[0]) for p in PROVINCIAS_VALPARAISO])
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Campo dinámico para seleccionar un material típico
        try:
            queryset = Material.objects.all().order_by('categoria', 'nombre')
            # Selección múltiple de materiales (no placeholder). Se ajusta tamaño/estilo del widget
            self.fields['material'] = forms.ModelMultipleChoiceField(
                queryset=queryset,
                required=False,
                label='Materiales en mente a utilizar',
                widget=forms.SelectMultiple(attrs={
                    'size': 8,
                    'style': 'width:360px;',
                    'class': 'materials-select'
                })
            )
        except Exception:
            # En caso de que la base de datos no esté disponible durante import/migrations
            self.fields['material'] = forms.MultipleChoiceField(
                choices=[],
                required=False,
                label='Materiales en mente a utilizar',
                widget=forms.SelectMultiple(attrs={
                    'size': 8,
                    'style': 'width:360px;',
                    'class': 'materials-select'
                })
            )
