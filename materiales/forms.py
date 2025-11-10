from django import forms
from materiales.models import ProvinciaDatos

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
