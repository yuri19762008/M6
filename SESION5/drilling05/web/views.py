from django.shortcuts import render
from .services import lista_libros


def index(request):
    context = {}
    return render(request, "index.html", context)

def navbar(request):
    context = {}
    return render(request, "navbar.html", context)

def listbook(request):
    context = {"libros": lista_libros}
    return render(request, "listbook.html", context)


