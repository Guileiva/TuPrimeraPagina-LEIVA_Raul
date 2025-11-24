from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, DetailView, UpdateView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db.models import Q

from .models import Libro, Resena, Anuncio
from .forms import LibroForm, ResenaForm

def inicial(request):
    return render(request, 'index.html')

def es_superusuario(user):
    return user.is_superuser

# ------- CODIGO PARA LA GESTION DEL LIBRO ------- #

@login_required
def crear_libro(request):
    if not request.user.is_superuser:
        messages.error(request, "Acceso denegado. Solo administradores pueden crear libros.")
        return redirect('inicio') 
        
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)

        try:
            if form.is_valid():
                libro = form.save(commit=False)
                libro.usuario = request.user
                libro.save()
                return redirect('detalle_libro', pk=libro.pk)  
                
        except Exception as e:
            print(f"Ocurrio un error al crear el libro {e}")       
    else:
        form = LibroForm()

    return render(request, 'crear_libro.html', {'form': form})


class ListaLibros(ListView):
    model = Libro 
    context_object_name = 'libros' 
    template_name = 'listar_libros.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        
        if query:
            object_list = self.model.objects.filter(
                Q(titulo__icontains=query) | Q(autor__icontains=query)
            ).order_by('-fecha_publicacion')
        else:
            object_list = self.model.objects.all().order_by('-fecha_publicacion')
        return object_list

class DetalleLibro(DetailView):
    model = Libro
    context_object_name = 'libro'
    template_name = 'detalle_libro.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reseñas'] = self.object.reseñas.all()
        context['form_reseña'] = ResenaForm() 
        return context
    
class ModificarLibro(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Libro
    form_class = LibroForm 
    template_name = 'modificar_libro.html'

    def test_func(self):
        return self.request.user.is_superuser
               
    def get_success_url(self):
        return reverse_lazy('detalle_libro', kwargs={'pk': self.object.pk})
    

class EliminarLibro(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Libro
    template_name = 'eliminar_libro.html' 
    success_url = reverse_lazy('lista_libros') 

    def test_func(self):
        return self.request.user.is_superuser

# ------- CODIGO PARA LA GESTION DE RESEÑAS ------- #

@login_required 
def crear_resena(request, libro_pk):
    libro = get_object_or_404(Libro, pk=libro_pk)
    
    if Resena.objects.filter(libro=libro, usuario=request.user).exists():
        messages.warning(request, "Ya has dejado una reseña para este libro. Solo se permite una por usuario.")
        return redirect('detalle_libro', pk=libro_pk)
    
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        
        if form.is_valid():
            resena = form.save(commit=False) 
            resena.libro = libro
            resena.usuario = request.user
            resena.save() 
            messages.success(request, "¡Tu reseña ha sido publicada con éxito!")
            return redirect('detalle_libro', pk=libro_pk) 
        else:
            
            messages.error(request, "Error al enviar la reseña. Revisa los campos.")
            return redirect('detalle_libro', pk=libro_pk) 

    
    return redirect('detalle_libro', pk=libro_pk)


class ModificarResena(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Resena
    form_class = ResenaForm 
    template_name = 'modificar_resena.html' 
    context_object_name = 'resena'    
    
    def test_func(self):
        resena = self.get_object()
        return self.request.user == resena.usuario or self.request.user.is_superuser
        
    def get_success_url(self):
        return reverse_lazy('detalle_libro', kwargs={'pk': self.object.libro.pk})
    
        
class EliminarResena(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resena
    template_name = 'eliminar_resena.html'
    context_object_name = 'resena'
    
    def test_func(self):
        resena = self.get_object()
        return self.request.user == resena.usuario or self.request.user.is_superuser
   
    def get_success_url(self):
        libro_pk = self.get_object().libro.pk
        return reverse_lazy('detalle_libro', kwargs={'pk': libro_pk})
    
# ------- CODIGO PARA NOSOTROS ------- #

def nosotros(request):
    return render(request, 'nosotros.html')

# ------- CODIGO PARA LOS ANUNCIOS ------- #

class AnunciosListView(ListView):
    model = Anuncio
    template_name = 'anuncios_placeholder.html'
    context_object_name = 'anuncios'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
              
        novedades_ordenadas = Anuncio.objects.all().order_by('-fecha')
               
        context['noticia_principal'] = novedades_ordenadas.first()
               
        if novedades_ordenadas.count() > 0:
            context['otras_novedades'] = novedades_ordenadas[1:6] 
        else:
            context['otras_novedades'] = []

        return context

class AnuncioDetailView(DetailView):
    model = Anuncio
    template_name = 'detalle_anuncio.html'
    context_object_name = 'anuncio'




