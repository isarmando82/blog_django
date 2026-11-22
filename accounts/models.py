from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    """Informacion extra de cada usuario: biografia, web y avatar."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    biografia = models.TextField(blank=True)
    link_web = models.URLField(blank=True)
    avatar = models.ImageField(upload_to="avatares/", null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"