<<<<<<< HEAD
from django.contrib import admin
from .models import Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    search_fields = ['nome', 'tipo']
=======
from django.contrib import admin

# Register your models here.
>>>>>>> 4485df0c55ab9710514919aa953db86e5a9d4ee4
