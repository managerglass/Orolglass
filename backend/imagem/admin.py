from django.contrib import admin
from .models import Imagem


@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'tipo')
    search_fields = ['titulo', 'arquivo', 'tipo']
    