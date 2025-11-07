from django.shortcuts import render


def inicial(request):
    return render(request, 'index.html')

def crear_libro(request):
    return render(request, 'crear_libro.html')

def listado_libros(request):
    return render(request, 'listar_libros.html')
