from django.db import models
from backend.core.models import HerancaPadrao
from backend.imagem.models import Imagem
from backend.categoria.models import Categoria


class Evento(HerancaPadrao):
    tipo = models.ForeignKey(
        Categoria,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False
    )
    titulo = models.CharField(
        'Titulo do evento',
        max_length=100,
        blank=False,
        null=False
    )
    descricao = models.TextField()
    data = models.DateField()
    imagens = models.ManyToManyField(
        Imagem
    )

    class Meta:
        ordering = ('titulo', )
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    
    def __str__(self):
        return f'{self.titulo} - {self.data}'
