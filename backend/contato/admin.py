<<<<<<< HEAD
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
=======
from django.contrib import admin

# Register your models here.
>>>>>>> 4485df0c55ab9710514919aa953db86e5a9d4ee4
