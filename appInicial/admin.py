from django.contrib import admin
from .models import Libro, Resena, Anuncio

admin.site.register(Libro)
admin.site.register(Resena)
@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    list_filter = ('fecha',)
    search_fields = ('titulo', 'contenido')




