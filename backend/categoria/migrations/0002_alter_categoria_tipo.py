# Generated by Django 5.0.4 on 2024-04-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("categoria", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoria",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("IMAGEM", "Imagem"),
                    ("DESTAQUE", "Destaque"),
                    ("PROJETO", "Projeto"),
                    ("EVENTO", "Evento"),
                    ("CONTATO", "Contato"),
                    ("SOBRE", "Sobre"),
                ],
                max_length=20,
                verbose_name="Tipo de Categoria",
            ),
        ),
    ]