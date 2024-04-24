from django.contrib import admin
from .models import Projeto

#titulo, descrição, tipo, data, imagem manytomany
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'data')
    search_fields = ['titulo', 'tipo', 'data']
    