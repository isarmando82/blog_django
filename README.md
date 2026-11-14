# Blog Django

Proyecto base de un blog web desarrollado con Django.

Pre-entregas 7 y 8 — Curso de Python, Coderhouse

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
| `/` | Inicio: título, bienvenida y descripción del proyecto | `inicio` | `posts/inicio.html` |
| `/acerca/` | Acerca de: reseña del autor y propósito del sitio | `acerca` | `posts/acerca.html` |
| `/posts/` | Lista de publicaciones de ejemplo | `lista_posts` | `posts/lista_posts.html` |

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
    │   └── __init__.py
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

## Aplicaciones

- `posts`: aplicación principal del blog. Contiene las views, las rutas, los templates y los archivos estáticos del sitio.

## Archivos ignorados

El archivo `.gitignore` evita subir al repositorio el entorno virtual (`venv/`), los archivos temporales de Python (`__pycache__/`, `*.pyc`), las variables privadas (`.env`) y la base de datos local (`db.sqlite3`).
