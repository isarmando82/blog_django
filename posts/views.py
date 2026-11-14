from django.shortcuts import render


def inicio(request):
    """Muestra la pagina de inicio del blog."""
    return render(request, 'posts/inicio.html')


def acerca(request):
    """Muestra la pagina 'Acerca de' con la resena del autor."""
    return render(request, 'posts/acerca.html')


def lista_posts(request):
    """Muestra una lista de ejemplo de publicaciones.
    Todavia no hay base de datos: los posts se escriben directo en el template."""
    return render(request, 'posts/lista_posts.html')
