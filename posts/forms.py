from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Formulario basado en el modelo Post."""

    class Meta:
        model = Post
        fields = ["titulo", "contenido", "autor", "estado", "imagen"]