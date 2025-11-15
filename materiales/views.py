import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ProvinciaDatos, Material
from .forms import ProvinciaForm, PROVINCIAS_VALPARAISO
from collections import defaultdict

@login_required
def elegir_provincia(request):
    if request.method == "POST":
        form = ProvinciaForm(request.POST)
        if form.is_valid():
            provincia = form.cleaned_data["provincia"]
            materiales_seleccionados = form.cleaned_data.get('material')
            # Validación server-side: exigir al menos un material seleccionado
            if not materiales_seleccionados or (hasattr(materiales_seleccionados, '__len__') and len(materiales_seleccionados) == 0):
                form.add_error('material', 'Por favor seleccionar al menos un material')
                return render(request, "materiales/elegir_provincia.html", {"form": form})
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
            # Guardar selección de materiales si existe (many-to-many)
            try:
                if materiales_seleccionados:
                    registro.materials.set(materiales_seleccionados)
                else:
                    registro.materials.clear()
            except Exception:
                # en caso de que la relación no exista (migraciones pendientes), ignorar
                pass
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

    analysis = None
    if registro:
        # materiales seleccionados por el usuario (si se guardaron)
        try:
            seleccionados = list(registro.materials.all())
        except Exception:
            seleccionados = []

        # Preparar recomendaciones: para cada material seleccionado, buscar alternativas "naturales"
        recommendations = []
        if seleccionados:
            # usar todos los materiales como candidatos (no solo la categoría 'naturales')
            candidatos = list(Material.objects.all())
            for sel in seleccionados:
                # vector de relevancias del material seleccionado
                sv = (sel.relevancia_temperatura, sel.relevancia_radiacion, sel.relevancia_viento)
                scored = []
                for cand in candidatos:
                    if cand.pk == sel.pk:
                        continue
                    cv = (cand.relevancia_temperatura, cand.relevancia_radiacion, cand.relevancia_viento)
                    # distancia euclidiana entre vectores de relevancia
                    dist = ((sv[0]-cv[0])**2 + (sv[1]-cv[1])**2 + (sv[2]-cv[2])**2) ** 0.5
                    # penalización simple por clima: si la provincia es caliente, preferir candidatos con mayor relevancia_temperatura
                    climate_pen = 0
                    try:
                        if registro.temp_avg and registro.temp_avg >= 25:
                            # si candidato tiene menor relevancia de temperatura que el seleccionado, añadir penalidad
                            climate_pen = max(0, (sv[0] - cv[0])) * 0.3
                    except Exception:
                        climate_pen = 0
                    score = dist + climate_pen
                    scored.append((score, cand))
                # ordenar por score ascendente y tomar top 3
                scored.sort(key=lambda x: x[0])
                top = [c[1] for c in scored[:3]]
                recommendations.append({
                    'selected': sel,
                    'alternatives': top
                })

        analysis = {
            'registro': registro,
            'seleccionados': seleccionados,
            'recommendations': recommendations,
        }

    return render(request, "materiales/datos_terreno.html", {"registro": registro, 'analysis': analysis})

def lista_materiales(request):
    materiales = Material.objects.all().order_by('categoria', 'nombre')
    
    categorias = {}
    for material in materiales:
        key = material.get_categoria_display()  
        if key not in categorias:
            categorias[key] = []
        categorias[key].append(material)
    
    return render(request, 'materiales/lista_materiales.html', {'categorias': categorias})
