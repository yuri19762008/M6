
# Create your views here.

from .services import lista_libros
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Profile

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
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                email=form.cleaned_data.get('email')
            )
            messages.success(request, f'¡Cuenta creada exitosamente!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def listbook(request):
    libros_valorados = [libro for libro in lista_libros if libro.valoracion > 1500]
    context = {
        'libros_valorados': libros_valorados,
        'todos_los_libros': lista_libros
    }
    return render(request, 'libros/listbook.html', context)

from django.contrib.auth.decorators import permission_required

@login_required
@permission_required('libros.development', raise_exception=True)
def listbook(request):
    libros_valorados = [libro for libro in lista_libros if libro.valoracion > 1500]
    context = {
        'libros_valorados': libros_valorados,
        'todos_los_libros': lista_libros
    }
    return render(request, 'libros/listbook.html', context)