from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def es_palindromo(frase):
    # Elimina espacios y convierte a minúsculas
    frase = ''.join(frase.split()).lower()
    # Compara la frase con su reverso
    return frase == frase[::-1]

def palindromo(request, palabra):
    if es_palindromo(palabra):
        mensaje = f'"{palabra}" ES PALÍNDROMO'
    else:
        mensaje = f'"{palabra}" NO ES PALÍNDROMO'
    return HttpResponse(mensaje)
