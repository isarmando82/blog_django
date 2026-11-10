# Blog Django

Proyecto base de un blog web desarrollado con Django.

Pre-entrega 7 — Curso de Python, Coderhouse

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

Se tiene que ver la pantalla inicial de Django. Para detener el servidor, presionar `Ctrl + C`.

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
    └── views.py
```

## Aplicaciones

- `posts`: aplicación inicial para manejar las publicaciones del blog.

## Archivos ignorados

El archivo `.gitignore` evita subir al repositorio el entorno virtual (`venv/`), los archivos temporales de Python (`__pycache__/`, `*.pyc`), las variables privadas (`.env`) y la base de datos local (`db.sqlite3`).
