from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


def inicio(request):
    """Muestra la pagina de inicio con los ultimos 3 posts publicados."""
    ultimos_posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")[:3]
    context = {"posts": ultimos_posts}
    return render(request, "posts/inicio.html", context)


def acerca(request):
    """Muestra la pagina 'Acerca de' con la resena del autor."""
    return render(request, "posts/acerca.html")


def lista_posts(request):
    """Lista todos los posts para poder gestionarlos desde el sitio."""
    posts = Post.objects.all().order_by("-fecha_creacion")
    context = {"posts": posts}
    return render(request, "posts/lista_posts.html", context)


def detalle_post(request, pk):
    """Muestra un post individual con su imagen, si tiene."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/detalle_post.html", {"post": post})


@login_required
def crear_post(request):
    """Crea un post nuevo. Procesa texto (request.POST) e imagen (request.FILES)."""
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect("detalle_post", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "posts/post_form.html", {"form": form, "accion": "Crear"})


@login_required
def editar_post(request, pk):
    """Edita un post existente, permitiendo cambiar la imagen."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("detalle_post", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "posts/post_form.html", {"form": form, "accion": "Editar"})


@login_required
def eliminar_post(request, pk):
    """Pide confirmacion antes de borrar un post."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("lista_posts")
    return render(request, "posts/post_confirm_delete.html", {"post": post})