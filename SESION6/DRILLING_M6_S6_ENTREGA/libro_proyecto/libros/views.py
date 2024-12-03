
# Create your views here.
from django.shortcuts import render
from .services import lista_libros

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