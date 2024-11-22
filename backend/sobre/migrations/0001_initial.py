# Generated by Django 5.0.4 on 2024-04-24 15:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("imagem", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sobre",
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
                ("sobre", models.TextField()),
                ("valores", models.TextField()),
                ("lema", models.TextField()),
                ("missao", models.TextField()),
                ("visao", models.TextField()),
                ("crenca", models.TextField()),
                ("imagens", models.ManyToManyField(to="imagem.imagem")),
            ],
            options={
                "verbose_name": "Sobre",
                "verbose_name_plural": "Sobre",
            },
        ),
    ]
