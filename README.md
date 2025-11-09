## Bookish Online: Plataforma de Reseñas y Catálogo Literario

Este proyecto es una aplicación web desarrollada con Django y Bootstrap 5, siguiendo el patrón MVT, para gestionar y publicar un catálogo de reseñas de libros online.

### 🛠️ Configuración Inicial

1. Clona o descarga el repositorio: `git git clone https://github.com/Guileiva/TuPrimeraPagina-LEIVA_Raul.git`
2. Crea y activa el entorno virtual: `python -m venv .venv` - `. .venv/Scripts/activate`
3. Instala las dependencias: `pip install -r requirements.txt`.
4. Prepara y aplica los cambios de las migraciones: 
    * a) `python manage.py makemigrations`
    * b) `python manage.py migrate`
5. Ejecuta el servidor: `python manage.py runserver`

### 📋 Orden de Prueba y Funcionalidades

Las principales funcionalidades del proyecto se prueban en el siguiente orden:

1.  **Página Principal:** Accede a `http://127.0.0.1:8000/`. Desde aquí, puedes navegar a las dos funciones principales.
2.  **Crear Reseña:**
    * Ve a la URL: `/crear-libro/` (o haz clic en "**Catálogo de Reseñas**" en la barra de navegación).
    * El formulario solo requiere el **Título**, **Autor** y la **Descripción/Sinopsis** del libro.
3.  **Catalogo de Reseñas:**
    * Ve a la URL: `/listar-libros/` (o haz clic en "Catálogo de Reseñas" en la barra de navegación).
    * Esta vista (`listar_libros`) muestra todos los posts guardados.
4.  **Una breve historia sobre nosotros:**

