from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Perfil


class RegistroForm(UserCreationForm):
    """Formulario de registro personalizado: suma email, nombre y apellido."""

    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class UsuarioForm(forms.ModelForm):
    """Datos basicos del usuario que se pueden editar."""

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        labels = {"first_name": "Nombre", "last_name": "Apellido"}


class PerfilForm(forms.ModelForm):
    """Biografia, web y avatar del perfil."""

    class Meta:
        model = Perfil
        fields = ["biografia", "link_web", "avatar"]