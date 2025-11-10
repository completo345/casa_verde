from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistroForm

# Registro de usuario
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registro_user/registro.html', {'form': form})

# Login de usuario
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    else:
        form = AuthenticationForm()
    return render(request, 'registro_user/login.html', {'form': form})

# Create your views here.
# help me plaese


















# leave me alone
