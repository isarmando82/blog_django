"""
URL configuration for blog_project project.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Rutas de la app posts
    path("", include("posts.urls")),
    # Rutas de la app accounts
    path("cuentas/", include("accounts.urls")),
]

# Servir archivos media (imagenes subidas) durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
