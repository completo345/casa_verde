import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ProvinciaDatos
from .forms import ProvinciaForm, PROVINCIAS_VALPARAISO

@login_required
def elegir_provincia(request):
    if request.method == "POST":
        form = ProvinciaForm(request.POST)
        if form.is_valid():
            provincia = form.cleaned_data["provincia"]
            lat, lon = dict(PROVINCIAS_VALPARAISO)[provincia]

            # NASA POWER API — últimos 5 años
            url = (
                f"https://power.larc.nasa.gov/api/temporal/climatology/point?"
                f"parameters=T2M,ALLSKY_SFC_SW_DWN,WS2M&community=RE"
                f"&longitude={lon}&latitude={lat}&format=JSON"
            )

            response = requests.get(url).json()
            data = response["properties"]["parameter"]

            temp_avg = sum(data["T2M"].values()) / len(data["T2M"])
            irr_avg = sum(data["ALLSKY_SFC_SW_DWN"].values()) / len(data["ALLSKY_SFC_SW_DWN"])
            wind_avg = sum(data["WS2M"].values()) / len(data["WS2M"])

            registro, created = ProvinciaDatos.objects.update_or_create(
                user=request.user,
                defaults={
                    "provincia": provincia,
                    "lat": lat,
                    "lon": lon,
                    "temp_avg": temp_avg,
                    "irr_avg": irr_avg,
                    "wind_avg": wind_avg
                }
            )

            return redirect("datos_terreno")

    else:
        form = ProvinciaForm()

    return render(request, "materiales/elegir_provincia.html", {"form": form})

@login_required
def datos_terreno(request):
    try:
        registro = ProvinciaDatos.objects.get(user=request.user)
    except ProvinciaDatos.DoesNotExist:
        registro = None

    return render(request, "materiales/datos_terreno.html", {"registro": registro})

