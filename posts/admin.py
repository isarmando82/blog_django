from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    """Configura como se ve el modelo Post en el panel de administracion."""

    # Columnas que se muestran en el listado del admin
    list_display = ("titulo", "autor", "estado", "fecha_creacion")
    # Filtro lateral por estado
    list_filter = ("estado",)
    # Buscador por titulo y autor
    search_fields = ("titulo", "autor")


admin.site.register(Post, PostAdmin)
