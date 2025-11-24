from django.contrib import admin
from .models import Libro, Resena, Anuncio

admin.site.register(Libro)
admin.site.register(Resena)
@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    # Campos que se muestran en el listado de anuncios en el admin
    list_display = ('titulo', 'fecha')
    
    # Filtros laterales
    list_filter = ('fecha',)
    
    # Campos que permiten la búsqueda
    search_fields = ('titulo', 'contenido')




