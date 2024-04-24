from django.contrib import admin
from .models import Contato


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
        'contato',
        'tipo',
        'observacao'
    ]
    search_fields = [
        'titulo',
        'contato'
    ]
