from django.urls import path
from appInicial.views import inicial, crear_libro, listado_libros

urlpatterns = [
    path('', inicial),
    path('crear-libro/', crear_libro),
    path('listar-libros/', listado_libros),
]