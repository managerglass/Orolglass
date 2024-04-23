from backend.core.models import HerancaPadrao
from backend.categoria.models import Categoria
from django.db import models


class Contato(HerancaPadrao):
    tipo = models.ForeignKey(
        Categoria,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False
    )
    titulo = models.CharField(
        'Título do Contato',
        max_length=100,
        blank=False,
        null=False
    )
    observacao = models.CharField(
        'Observação do contato',
        max_length=256,
        blank=True,
        null=True
    )
    contato = models.CharField(
        'Contato(email, telefone, link)',
        max_length=256,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ('titulo', )
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
    
    def __str__(self):
        return f'{self.titulo}: {self.contato}'
