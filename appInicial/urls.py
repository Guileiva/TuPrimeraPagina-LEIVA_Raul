from django.urls import path
from appInicial.views import inicial, crear_libro, listado_libros, nosotros

urlpatterns = [
    path('', inicial, name='inicio'),
    path('crear-libro/', crear_libro, name='crear_libro'),
    path('listar-libros/', listado_libros, name='lista_libros'),
    path('acerca/', nosotros, name='sobre_nosotros'),
]