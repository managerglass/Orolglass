from django.db import models
from backend.core.models import HerancaPadrao


class Endereco(HerancaPadrao):
    endereco = models.CharField(
        'Endereço ja formatado',
        max_length=256,
    )
    funcionamento = models.CharField(
        'Horario de Funcionamento ja formatado',
        max_length=256
    )
    redirecionamento = models.TextField(
        'Link para google MAPS',
    )
    tipo = models.CharField(
        'Tipo (loja ou Fábrica)',
        max_length=50
    )

    class Meta:
        ordering = ('tipo', )
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
    
    def __str__(self) -> str:
        return f'{self.tipo} - {self.endereco} {self.funcionamento}'
