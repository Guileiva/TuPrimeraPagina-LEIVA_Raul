## Bookish Online: Sistema de Gestión de Inventario

Este proyecto es una aplicación web desarrollada con Django y Bootstrap 5, siguiendo el patrón MVT, para gestionar el inventario de una pequeña librería.

### 🛠️ Configuración Inicial

1. Clona o descarga el repositorio: `git git clone https://github.com/Guileiva/TuPrimeraPagina-LEIVA_Raul.git`
2. Crea y activa el entorno virtual: `python -m venv .venv` - `. .venv/Scripts/activate`
3. Instala las dependencias: `pip install -r requirements.txt`.
4. Prepara y aplica los cambios de las migraciones: `a) python manage.py makemigrations b) python manage.py migrate`
5. Ejecuta el servidor: `python manage.py runserver`

### 📋 Orden de Prueba y Funcionalidades

Las principales funcionalidades del proyecto se prueban en el siguiente orden:

1.  **Página Principal (Home):** Accede a `http://127.0.0.1:8000/`. Desde aquí, puedes navegar a las dos funciones principales.
2.  **Cargar Libro:**
    * Ve a la URL: `/crear-libro/` (o haz clic en "Cargar Libro" en la barra de navegación).
    * Inserta Título, Autor, Precio y Stock. El formulario maneja la inserción de datos.
3.  **Listado de Libros:**
    * Ve a la URL: `/listar-libros/` (o haz clic en "Ver Libros" en la barra de navegación).
    * Esta vista (`listar_libros`) muestra todos los libros guardados en la BD.
4.  **Una breve historia sobre nosotros:**

