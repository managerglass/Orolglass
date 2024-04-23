from django.contrib import admin
from .models import Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'rede_social',
        'relato',
        'contato',
        'criado_em',
    ]
    search_fields = [
        'nome',
        'rede_social'
    ]