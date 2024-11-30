

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Libro
from .forms  import LibroForm

class ListadoLibros(ListView):
    model = Libro
    template_name = 'libros/listado_libros.html'
    context_object_name = 'libros'
    ordering = ['titulo']

class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/crear_libro.html'
    success_url = reverse_lazy('listado_libros')

class ActualizarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/actualizar_libro.html'
    success_url = reverse_lazy('listado_libros')

class EliminarLibro(DeleteView):
    model = Libro
    template_name = 'libros/eliminar_libro.html'
    success_url = reverse_lazy('listado_libros')