from django.urls import path
from appInicial.views import inicial, crear_libro, nosotros, crear_resena
from appInicial import views as app_views

urlpatterns = [
    path('', inicial, name='inicio'),
    path('libros/crear/', crear_libro, name='crear_libro'),
    path('libros/', app_views.ListaLibros.as_view(), name='lista_libros'),
    path('libros/<int:pk>/', app_views.DetalleLibro.as_view(), name='detalle_libro'),
    path('libros/<int:pk>/editar/', app_views.ModificarLibro.as_view(), name='editar_libro'),
    path('libros/<int:pk>/eliminar/', app_views.EliminarLibro.as_view(), name='eliminar_libro'),
    path('libros/<int:libro_pk>/resena/crear/', crear_resena, name='crear_resena'),
    path('resenas/<int:pk>/modificar/', app_views.ModificarResena.as_view(), name='modificar_resena'),
    path('resenas/<int:pk>/eliminar/', app_views.EliminarResena.as_view(), name='eliminar_resena'),
    path('anuncios/', app_views.AnunciosListView.as_view(), name='lista_anuncios'),
    path('anuncios/<int:pk>/', app_views.AnuncioDetailView.as_view(), name='detalle_anuncio'),
    path('acerca/', nosotros, name='sobre_nosotros'),
   
]