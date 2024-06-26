"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/v1/',
        include('backend.categoria.urls')
    ),
    path(
        'api/v1/',
        include('backend.avaliacao.urls')
    ),
    path(
        'api/v1/',
        include('backend.contato.urls')
    ),
    path(
        'api/v1/',
        include('backend.imagem.urls')
    ),
    path(
        'api/v1/',
        include('backend.destaque.urls')
    ),
    path(
        'api/v1/',
        include('backend.projeto.urls')
    ),
    path(
        'api/v1/',
        include('backend.sobre.urls')
    ),
    path(
        'api/v1/',
        include('backend.evento.urls')
    ),
    path(
        'api/v1/',
        include('backend.endereco.urls')
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
