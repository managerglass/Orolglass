# Generated by Django 5.0.4 on 2024-04-25 11:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Endereco",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("modificado_em", models.DateTimeField(auto_now_add=True)),
                ("ativo", models.BooleanField(default=True)),
                (
                    "endereco",
                    models.CharField(
                        max_length=256, verbose_name="Endereço ja formatado"
                    ),
                ),
                (
                    "funcionamento",
                    models.CharField(
                        max_length=256,
                        verbose_name="Horario de Funcionamento ja formatado",
                    ),
                ),
                (
                    "redirecionamento",
                    models.TextField(verbose_name="Link para google MAPS"),
                ),
                (
                    "tipo",
                    models.CharField(
                        max_length=50, verbose_name="Tipo (loja ou Fábrica)"
                    ),
                ),
            ],
            options={
                "verbose_name": "Endereço",
                "verbose_name_plural": "Endereços",
                "ordering": ("tipo",),
            },
        ),
    ]