

# Register your models here.
from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'fecha_publicacion')
    search_fields = ('titulo', 'autor', 'isbn')
    list_filter = ('fecha_publicacion',)