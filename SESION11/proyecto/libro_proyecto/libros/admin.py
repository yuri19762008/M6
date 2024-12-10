

# Register your models here.
from django.contrib import admin
from .models import Libro

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'valoracion', 'fecha_creacion', 'fecha_modificacion')
    search_fields = ('titulo', 'autor')

admin.site.register(Libro, LibroAdmin)

# Personalizar títulos del admin
admin.site.site_header = 'Administración de Libros'
admin.site.index_title = 'Panel de Control'
admin.site.site_title = 'Biblioteca Django'