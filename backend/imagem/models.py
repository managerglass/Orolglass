from django.db import models
from backend.core.models import HerancaPadrao
from backend.categoria.models import Categoria


class Imagem(HerancaPadrao):
    titulo = models.CharField(
        'Titulo',
        max_length=20,
        blank=False,
        null=False
    )
    arquivo = models.FileField(
        upload_to='imagens',
    )
    tipo = models.ForeignKey(
        Categoria,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False
    ) 
