from django.contrib import admin
from .models import Sobre


@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = [
        'sobre',
        'valores',
        'lema',
        'missao',
        'visao',
        'crenca'
    ]
