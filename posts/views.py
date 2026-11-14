from django.shortcuts import render

from .models import Post


def inicio(request):
    """Muestra la pagina de inicio con los ultimos 3 posts publicados."""
    ultimos_posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")[:3]
    context = {
        "posts": ultimos_posts
    }
    return render(request, "posts/inicio.html", context)


def acerca(request):
    """Muestra la pagina 'Acerca de' con la resena del autor."""
    return render(request, "posts/acerca.html")


def lista_posts(request):
    """Consulta los posts publicados en la base de datos y los envia al template."""
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    context = {
        "posts": posts
    }
    return render(request, "posts/lista_posts.html", context)
