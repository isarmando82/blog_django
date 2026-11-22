from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import PerfilForm, RegistroForm, UsuarioForm
from .models import Perfil


def registro(request):
    """Crea un usuario nuevo y su perfil, y lo manda al login."""
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Perfil.objects.create(user=usuario)
            return redirect("login")
    else:
        form = RegistroForm()
    return render(request, "accounts/registro.html", {"form": form})


@login_required
def perfil(request):
    """Muestra el perfil del usuario logueado."""
    perfil_usuario, _ = Perfil.objects.get_or_create(user=request.user)
    return render(request, "accounts/perfil.html", {"perfil": perfil_usuario})


@login_required
def editar_perfil(request):
    """Edita nombre, apellido, email, biografia y avatar (usa request.FILES)."""
    perfil_usuario, _ = Perfil.objects.get_or_create(user=request.user)
    if request.method == "POST":
        usuario_form = UsuarioForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil_usuario)
        if usuario_form.is_valid() and perfil_form.is_valid():
            usuario_form.save()
            perfil_form.save()
            return redirect("perfil")
    else:
        usuario_form = UsuarioForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil_usuario)
    context = {"usuario_form": usuario_form, "perfil_form": perfil_form}
    return render(request, "accounts/editar_perfil.html", context)
