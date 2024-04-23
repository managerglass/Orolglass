from django.db import models
from backend.core.models import HerancaPadrao


TIPO_CATEGORIA = [
    ('IMAGEM', 'Imagem'),
    ('DESTAQUE', 'Destaque')
]


class Categoria(HerancaPadrao):
    tipo = models.CharField(
        'Tipo de Categoria',
        max_length=20,
        choices=TIPO_CATEGORIA
    )
    nome = models.CharField(
        'Nome da Categoria',
        max_length=50,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ('nome', )
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return f'{self.nome} - {self.tipo}'
