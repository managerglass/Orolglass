from django.contrib import admin
from .models import Destaque


@admin.register(Destaque)
class DestaqueAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
        'descricao',
        'tipo'
    ]
    search_fields = [
        'titulo',
        'tipo'
    ]