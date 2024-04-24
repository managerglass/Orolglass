import uuid
from django.db import models


class Uuid(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)

    class Meta:
        abstract = True


class TimeStamped(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Ativo(models.Model):
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class HerancaPadrao(Ativo, TimeStamped, Uuid):

    class Meta:
        abstract = True
