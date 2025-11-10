from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DatosTerreno
from .models import Material
from .forms import DatosTerrenoForm

@login_required
def editar_datos_terreno(request):
    try:
        datos = DatosTerreno.objects.get(usuario=request.user)
    except DatosTerreno.DoesNotExist:
        datos = None

    if request.method == 'POST':
        form = DatosTerrenoForm(request.POST, instance=datos)
        if form.is_valid():
            terreno = form.save(commit=False)
            terreno.usuario = request.user
            terreno.save()
            return redirect('home')
    else:
        form = DatosTerrenoForm(instance=datos)

    return render(request, 'materiales/editar_datos_terreno.html', {'form': form})

def lista_materiales(request):
    materiales = Material.objects.all().order_by('categoria', 'nombre')
    return render(request, 'materiales/lista_materiales.html', {'materiales': materiales})
