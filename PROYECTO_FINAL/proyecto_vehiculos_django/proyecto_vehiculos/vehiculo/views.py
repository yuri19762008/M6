from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import VehiculoForm
from .models import Vehiculo
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroUsuarioForm

def index(request):
    return render(request, 'vehiculo/index.html')

@login_required
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})

@login_required
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehiculos': vehiculos})


# Crear la vista de registro
#from django.shortcuts import render, redirect
#from django.contrib.auth import login
#from .forms import RegistroUsuarioForm

def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirige a la página de inicio después del registro
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro_usuario.html', {'form': form})

