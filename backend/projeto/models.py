from django.db import models
from backend.core.models import HerancaPadrao
from backend.imagem.models import Imagem
from backend.categoria.models import Categoria


class Projeto(HerancaPadrao, Categoria, Imagem):
    titulo = models.CharField(
        'Titulo',
        max_length=20,
        blank=False,
        null=False
    ),
    descricao = models.TextField(
        'Descrição',
        blank=False,
        null=False
    ),
    tipo = models.ForeignKey(
        Categoria,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False
    ),
    data = models.DateField(

    ),
    imagem = models.ManyToManyField(
        Imagem
    )


    class Meta:
        ordering = ('titulo', 'tipo')
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return f'({self.titulo} - {self.descricao} - {self.tipo} - {self.imagem})'
    
