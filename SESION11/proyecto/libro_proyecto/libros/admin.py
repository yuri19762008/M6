from django.contrib import admin
from .models import Libro

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'valoracion', 'get_rating')
    search_fields = ('titulo', 'autor')
    
    def get_rating(self, obj):
        if obj.valoracion < 1000:
            return 'Baja'
        elif 1000 <= obj.valoracion <= 2500:
            return 'Media'
        else:
            return 'Alta'
    
    get_rating.short_description = 'Rating'
    get_rating.admin_order_field = 'valoracion'

admin.site.register(Libro, LibroAdmin)
admin.site.site_header = 'Administración de Libros'
admin.site.index_title = 'Panel de Control'
admin.site.site_title = 'Biblioteca Django'