# Blog Django

Proyecto de un blog web desarrollado con Django.
Pre-entregas 7, 8, 9 y 10 — Curso de Python, Coderhouse
Autor: Armando Ismael

## Descripción

Blog con Django que permite crear, ver, editar y eliminar publicaciones desde el propio sitio, cada una con una imagen opcional. Incluye la configuración del proyecto `blog_project` y la aplicación `posts`.

Configuración aplicada en `blog_project/settings.py`:

- La app `posts` está registrada en `INSTALLED_APPS` como `'posts.apps.PostsConfig'`.
- Idioma: `LANGUAGE_CODE = 'es-ar'`.
- Zona horaria: `TIME_ZONE = 'America/Argentina/Buenos_Aires'`.
- Archivos media: `MEDIA_URL = '/media/'` y `MEDIA_ROOT = BASE_DIR / 'media'`.

## Requisitos

- Python 3.10 o superior.
- Git.
- Pillow (se instala con `requirements.txt`).

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

Activar el entorno virtual. En Windows PowerShell:

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

Levantar el servidor y entrar a `http://127.0.0.1:8000/admin/`. En la sección **Posts** se pueden gestionar las publicaciones, con filtro por estado y buscador.

## Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador: `http://127.0.0.1:8000/`

Para detener el servidor, presionar `Ctrl + C`.

## CRUD de posts

Desde el sitio se pueden realizar todas las operaciones sobre el modelo `Post`:

| Operación | Ruta | View | Template |
|---|---|---|---|
| Listar (Read) | `/posts/` | `lista_posts` | `posts/lista_posts.html` |
| Ver detalle (Read) | `/posts/<id>/` | `detalle_post` | `posts/detalle_post.html` |
| Crear (Create) | `/posts/crear/` | `crear_post` | `posts/post_form.html` |
| Editar (Update) | `/posts/<id>/editar/` | `editar_post` | `posts/post_form.html` |
| Eliminar (Delete) | `/posts/<id>/eliminar/` | `eliminar_post` | `posts/post_confirm_delete.html` |

Otras páginas:

| Ruta | Página |
|---|---|
| `/` | Inicio con los últimos 3 posts publicados |
| `/acerca/` | Acerca de: reseña del autor |
| `/admin/` | Panel de administración de Django |

- El listado muestra todos los posts con links para ver, editar y eliminar, y un botón **+ Nuevo post**.
- El borrado pide confirmación antes de eliminar, para evitar eliminaciones accidentales.
- Después de crear o editar, se redirige al detalle del post; después de eliminar, al listado.

## Formulario

En `posts/forms.py` está la clase `PostForm`, que hereda de `forms.ModelForm` y está basada en el modelo `Post`. Incluye los campos `titulo`, `contenido`, `autor`, `estado` e `imagen`. Se usa tanto para crear como para editar.

## Manejo de imágenes

1. **Dependencia nueva:** se instaló **Pillow** (`pip install Pillow`), necesaria para usar `ImageField`, y se actualizó `requirements.txt` con `pip freeze > requirements.txt`.
2. **Modelo:** se agregó al modelo `Post` el campo `imagen = models.ImageField(upload_to='posts/', null=True, blank=True)`. Es opcional, y las imágenes se guardan en `media/posts/`.
3. **Migraciones:** se ejecutaron `python manage.py makemigrations` (que generó `0002_post_imagen.py`) y `python manage.py migrate`.
4. **Configuración de media:** en `settings.py` se definieron `MEDIA_URL = '/media/'` y `MEDIA_ROOT = BASE_DIR / 'media'`.
5. **Servir media en desarrollo:** en `blog_project/urls.py` se agregó `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` cuando `DEBUG` está activo, para que las imágenes se vean en el navegador.
6. **Vistas:** `crear_post` y `editar_post` instancian el formulario con `PostForm(request.POST, request.FILES)`, así se procesan tanto los datos de texto como la imagen.
7. **Template del formulario:** la etiqueta `<form>` de `post_form.html` incluye `enctype="multipart/form-data"`, sin el cual la imagen no llega al servidor.
8. **Mostrar la imagen:** el listado y el detalle muestran la imagen solo si existe (`{% if post.imagen %}`). Si un post no tiene imagen, el template no se rompe: el detalle muestra el aviso "Este post no tiene imagen".

## Cómo probar la carga de imágenes

1. Levantar el servidor con `python manage.py runserver`.
2. Entrar a `http://127.0.0.1:8000/posts/` y hacer clic en **+ Nuevo post**.
3. Completar título, contenido, autor y estado, elegir una imagen y guardar.
4. Verificar que el detalle del post muestra la imagen.
5. Crear otro post sin imagen y verificar que se ve el aviso en lugar de la imagen.
6. Entrar a **Editar**, elegir otra imagen, guardar y verificar que se actualizó.
7. Entrar a **Eliminar**, confirmar, y verificar que el post ya no aparece en el listado.

## Cómo funciona: ruta → vista → template → estático

1. `blog_project/urls.py` conecta las rutas de la app con `include("posts.urls")`.
2. `posts/urls.py` define un `path()` para cada página y cada operación del CRUD.
3. `posts/views.py` tiene una función por página u operación, que devuelve su template con `render()` o redirige con `redirect()`.
4. Los templates hijos usan `{% extends 'posts/base.html' %}` y completan el `{% block content %}`.
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
├── media/
│   └── posts/
└── posts/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations/
    │   ├── __init__.py
    │   ├── 0001_initial.py
    │   └── 0002_post_imagen.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── templates/
    │   └── posts/
    │       ├── base.html
    │       ├── inicio.html
    │       ├── acerca.html
    │       ├── lista_posts.html
    │       ├── detalle_post.html
    │       ├── post_form.html
    │       └── post_confirm_delete.html
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
| `imagen` | `ImageField(upload_to='posts/', null=True, blank=True)` | Imagen opcional del post. |

El método `__str__` devuelve el título, así cada post se ve por su nombre en el admin.

La página de inicio muestra solo los últimos 3 posts publicados. El listado `/posts/` muestra todos los posts, incluidos borradores y archivados, para poder gestionarlos desde el sitio.

## Aplicaciones

- `posts`: aplicación principal del blog. Contiene el modelo, el formulario, las views, las rutas, los templates y los archivos estáticos del sitio.

## Archivos ignorados

El archivo `.gitignore` evita subir al repositorio el entorno virtual (`venv/`), los archivos temporales de Python (`__pycache__/`, `*.pyc`), las variables privadas (`.env`) y la base de datos local (`db.sqlite3`).