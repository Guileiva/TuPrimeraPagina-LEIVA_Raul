## Proyecto Final Curso Python - Coderhouse

Alumno: Leiva, Raul Guillermo  
Comision: 78335

## Bookish Online: Plataforma de Reseñas y Catálogo Literario

Este proyecto es una aplicación web desarrollada con Django y Bootstrap 5, siguiendo el patrón MVT, para gestionar y publicar un catálogo de reseñas de libros online.

## Video demostracion

https://youtu.be/T0neeS-5Qug


### 🛠️ Configuración Inicial

1. Clona o descarga el repositorio: `git git clone https://github.com/Guileiva/TuPrimeraPagina-LEIVA_Raul.git`
2. Crea y activa el entorno virtual: `python -m venv .venv` - `. .venv/Scripts/activate`
3. Instala las dependencias: `pip install -r requirements.txt`.
4. Prepara y aplica los cambios de las migraciones: 
    * a) `python manage.py makemigrations`
    * b) `python manage.py migrate`
5. Crea un Superusuario (Administrador): `python manage.py createsuperuser`
6. Ejecuta el servidor: `python manage.py runserver`

### 📋 Prueba y Funcionalidades

Las principales funcionalidades del proyecto son:

1.  **Página Principal:** Accede a `http://127.0.0.1:8000/`. Desde aquí, puedes explorar las distintas secciones, tanto desde la barra de navegacion como desde el cuerpo del Sitio.
2.  **Ver Catálogo de Libros:**
    * Ve a Explorar Catálogo (o haz clic en "**Catálogo de Libros**" en la barra de navegación).   

    2.1. **<ins>Ver o dejar reseñas:</ins>** Haz clic en el boton "Ver Detalles y Reseñas" para acceder al detalle del libro. (las reseñas solo estan disponible para usuarios logueados) 
        
3.  **Ver Anuncios y Novedades:**
    * Ve a la tarjeta Anuncios y Novedades (o haz clic en "**Anuncios y Novedades**" en la barra de navegación).    
4.  **Una breve historia sobre nosotros:**

Funcionalidades exclusivas con perfil de Administrador:

1.  **Añadir Nuevo Libro:** 
    * Ve a Añadir Nuevo Libro (o haz clic en "**Crear Libro**" en la barra de navegación).
    * El formulario requiere el Título, Autor y la Descripción/Sinopsis del libro, (opcional: agregar iamgen de portada)
2.  **Añadir Anuncios:**
    * Accede al panel de administracion de Django http://127.0.0.1:8000/admin/. 
    * Ve a "+ Añadir" en Anuncios.
    * El formulario requiere el Título y Contenido (opcional: se puede modificar fecha y hora de publicación)   
    
