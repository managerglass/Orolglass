from django.db import models
from backend.core.models import HerancaPadrao
from backend.imagem.models import Imagem


class Sobre(HerancaPadrao):
    imagens = models.ManyToManyField(
        Imagem,
    )
    sobre = models.TextField()
    valores = models.TextField()
    lema = models.TextField()
    missao = models.TextField()
    visao = models.TextField()
    crenca = models.TextField()

    class Meta:
        verbose_name = 'Sobre'
        verbose_name_plural = 'Sobre'
    
    def __str__(self) -> str:
        return {self.sobre}
