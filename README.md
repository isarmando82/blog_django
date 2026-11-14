# Blog Django

Proyecto base de un blog web desarrollado con Django.

Pre-entregas 7, 8 y 9 — Curso de Python, Coderhouse

Autor: Armando Ismael

## Descripción

Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog.
Incluye la configuración base del proyecto `blog_project` y una aplicación llamada `posts`.

Configuración aplicada en `blog_project/settings.py`:

- La app `posts` está registrada en `INSTALLED_APPS` como `'posts.apps.PostsConfig'`.
- Idioma: `LANGUAGE_CODE = 'es-ar'`.
- Zona horaria: `TIME_ZONE = 'America/Argentina/Buenos_Aires'`.

## Requisitos

- Python 3.10 o superior.
- Git.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/isarmando82/blog_django.git
```

Entrar a la carpeta del proyecto:

```bash
cd blog_django
```

Crear el entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual.

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Si PowerShell no deja ejecutar el script, correr antes:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

En Linux o macOS:

```bash
source venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Crear la base de datos

La base de datos local (`db.sqlite3`) no se sube al repositorio. Se crea aplicando las migraciones:

```bash
python manage.py migrate
```

## Panel de administración

Crear un superusuario (pide nombre de usuario, email y contraseña):

```bash
python manage.py createsuperuser
```

Levantar el servidor y entrar a:

```
http://127.0.0.1:8000/admin/
```

Ingresar con el superusuario. En la sección **Posts** se pueden crear, editar y borrar publicaciones. El listado muestra las columnas título, autor, estado y fecha de creación, con un filtro por estado y un buscador.

## Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

```
http://127.0.0.1:8000/
```

Para detener el servidor, presionar `Ctrl + C`.

## Páginas del sitio

| Ruta | Página | View | Template |
|---|---|---|---|
| `/` | Inicio: título, bienvenida, descripción y los últimos 3 posts publicados | `inicio` | `posts/inicio.html` |
| `/acerca/` | Acerca de: reseña del autor y propósito del sitio | `acerca` | `posts/acerca.html` |
| `/posts/` | Lista de los posts publicados, cargados desde la base de datos | `lista_posts` | `posts/lista_posts.html` |
| `/admin/` | Panel de administración de Django | — | — |

El menú de navegación está en `base.html` y permite moverse entre las páginas.

## Cómo funciona: ruta → vista → template → estático

1. `blog_project/urls.py` conecta las rutas de la app con `include("posts.urls")`.
2. `posts/urls.py` define un `path()` para cada página.
3. `posts/views.py` tiene una función por página, que devuelve su template con `render()`.
4. Los templates hijos (`inicio.html`, `acerca.html`, `lista_posts.html`) usan `{% extends 'posts/base.html' %}` y completan el `{% block content %}`.
5. `base.html` usa `{% load static %}` y enlaza el CSS con `{% static 'posts/css/estilos.css' %}`.

## Estructura del proyecto

```
blog_django/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── posts/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── templates/
    │   └── posts/
    │       ├── base.html
    │       ├── inicio.html
    │       ├── lista_posts.html
    │       └── acerca.html
    └── static/
        └── posts/
            └── css/
                └── estilos.css
```

## Modelo Post

Definido en `posts/models.py`:

| Campo | Tipo | Descripción |
|---|---|---|
| `titulo` | `CharField` | Título del post. |
| `contenido` | `TextField` | Texto de la publicación. |
| `autor` | `CharField` | Nombre de quien escribe. |
| `fecha_creacion` | `DateTimeField(auto_now_add=True)` | Se completa sola al crear el post. |
| `estado` | `CharField` con `choices` | `borrador`, `publicado` o `archivado`. |

El método `__str__` devuelve el título, así cada post se ve por su nombre en el admin.

La view `lista_posts` consulta con el ORM solo los posts publicados, del más nuevo al más viejo:

```python
Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
```

y el template `lista_posts.html` los recorre con `{% for post in posts %}`. Los borradores y los archivados no se muestran en el sitio.

## Aplicaciones

- `posts`: aplicación principal del blog. Contiene las views, las rutas, los templates y los archivos estáticos del sitio.

## Archivos ignorados

El archivo `.gitignore` evita subir al repositorio el entorno virtual (`venv/`), los archivos temporales de Python (`__pycache__/`, `*.pyc`), las variables privadas (`.env`) y la base de datos local (`db.sqlite3`).
