
from django.urls import path
from .views import ListadoLibros, CrearLibro, ActualizarLibro, EliminarLibro

urlpatterns = [
    path('', ListadoLibros.as_view(), name='listado_libros'),
    path('crear/', CrearLibro.as_view(), name='crear_libro'),
    path('actualizar/<int:pk>/', ActualizarLibro.as_view(), name='actualizar_libro'),
    path('eliminar/<int:pk>/', EliminarLibro.as_view(), name='eliminar_libro'),
]