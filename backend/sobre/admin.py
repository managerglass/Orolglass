from django.contrib import admin
from .models import (
    Sobre,
    Valores,
    Crencas
)


@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = [
        'sobre',
        'lema',
        'missao',
        'visao',
        'origem'
    ]

@admin.register(Valores)
class ValoresAdmin(admin.ModelAdmin):
    list_display = [
        'sobre',
        'valor',
    ]

@admin.register(Crencas)
class CrencasAdmin(admin.ModelAdmin):
    list_display = [
        'sobre',
        'crenca',
    ]
