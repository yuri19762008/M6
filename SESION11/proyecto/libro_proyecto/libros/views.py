
# Create your views here.

from .services import lista_libros
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .models import Profile
from .models import Libro

def index(request):
    return render(request, 'libros/index.html')

def listbook(request):
    libros_valorados = [libro for libro in lista_libros if libro.valoracion > 1500]
    context = {
        'libros_valorados': libros_valorados,
        'todos_los_libros': lista_libros
    }
    return render(request, 'libros/listbook.html', context)

def about(request):
    return render(request, 'libros/about.html')

def contact(request):
    return render(request, 'libros/contact.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Bienvenido {username}!')
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña inválidos.')
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Usuario {username} registrado exitosamente!')
            return redirect('login')
        else:
            messages.error(request, 'Error en el registro. Por favor, verifica los datos.')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def listbook(request):
    libros_valorados = Libro.objects.filter(valoracion__gt=1500)
    todos_los_libros = Libro.objects.all()
    
    context = {
        'libros_valorados': libros_valorados,
        'todos_los_libros': todos_los_libros
    }
    return render(request, 'libros/listbook.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, '¡Has cerrado sesión exitosamente!')
    return redirect('login')
