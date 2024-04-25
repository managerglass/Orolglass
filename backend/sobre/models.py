from django.db import models
from backend.core.models import HerancaPadrao
from backend.imagem.models import Imagem


class Sobre(HerancaPadrao):
    imagens = models.ManyToManyField(
        Imagem,
    )
    sobre = models.TextField()
    lema = models.TextField()
    missao = models.TextField()
    visao = models.TextField()
    origem = models.TextField()

    class Meta:
        verbose_name = 'Sobre'
        verbose_name_plural = 'Sobre'
    
    def __str__(self) -> str:
        return f'{self.sobre}'


class Valores(HerancaPadrao):
    sobre = models.ForeignKey(
        Sobre,
        on_delete=models.DO_NOTHING
    )
    valor = models.CharField(
        max_length=256
    )

    class Meta:
        ordering = ('valor', )
        verbose_name = 'Valores'
        verbose_name_plural = 'Valores'
    
    def __str__(self) -> str:
        return f'{self.valor}'


class Crencas(HerancaPadrao):
    sobre = models.ForeignKey(
        Sobre,
        on_delete=models.DO_NOTHING
    )
    crenca = models.CharField(
        max_length=256
    )

    class Meta:
        ordering = ('crenca', )
        verbose_name = 'Crenças'
        verbose_name_plural = 'Crenças'
    
    def __str__(self) -> str:
        return f'{self.crenca}'
    

