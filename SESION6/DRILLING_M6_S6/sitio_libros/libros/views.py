from django.shortcuts import render

# Create your from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def libros(request):
    return render(request, 'libros.html')

def acerca_de(request):
    return render(request, 'acerca_de.html')

def contacto(request):
    return render(request, 'contacto.html')