from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm

def inicial(request):
    return render(request, 'index.html')

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)

        try:
            if form.is_valid():
                form.save()
                return redirect('lista_libros')  
                
        except Exception as e:
            print(f"Ocurrio un error al crear el libro {e}")       
    else:
        form = LibroForm()

    return render(request, 'crear_libro.html', {'form': form})

def listado_libros(request):
    try:
        lista = Libro.objects.all().order_by('-pk')
        contexto = {'libros': lista}
    except Exception as e:
        print(f'Ocurrio un error al listar los libros {e}')

    return render(request, 'listar_libros.html', contexto)

def nosotros(request):
    return render(request, 'nosotros.html')




