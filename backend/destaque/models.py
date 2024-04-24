from django.db import models
from backend.core.models import HerancaPadrao
from backend.categoria.models import Categoria
from backend.imagem.models import Imagem


class Destaque(HerancaPadrao):
    tipo = models.ForeignKey(
        Categoria,
        on_delete=models.DO_NOTHING
    )
    titulo = models.CharField(
        'Titulo do Destaque',
        max_length=100,
        blank=False,
        null=False
    )
    descricao = models.CharField(
        'Descricao do Destaque',
        max_length=256,
        blank=True,
        null=True
    )
    imagem = models.ForeignKey(
        Imagem,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ('tipo', )
        verbose_name = 'Destaque'
        verbose_name_plural = 'Destaques'
    
    def __str__(self) -> str:
        return f'{self.titulo} - {self.descricao}'
