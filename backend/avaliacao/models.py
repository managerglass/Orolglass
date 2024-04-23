from django.db import models
from backend.core.models import HerancaPadrao


REDES_SOCIAIS = [
    ('FACEBOOK', 'Facebook'),
    ('INSTAGRAM', 'Instagram'),
    ('WHATSAPP', 'Whatsapp'),
]


class Avaliacao(HerancaPadrao):
    nome = models.CharField(
        'Nome da Pessoa',
        max_length=100,
        blank=False,
        null=False
    )
    rede_social = models.CharField(
        'Rede Social (opcional)',
        max_length=30,
        choices=REDES_SOCIAIS,
        blank=True,
        null=True
    )
    relato = models.TextField()
    contato = models.CharField(
        'Contato avaliador',
        max_length=50,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ('nome', )
        verbose_name = 'Avaliação'
        verbose_name = 'Avaliações'
    
    def __str__(self):
        return f'{self.nome} - {self.rede_social}'
