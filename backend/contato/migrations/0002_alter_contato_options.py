# Generated by Django 5.0.4 on 2024-09-02 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ('tipo',), 'verbose_name': 'Contato', 'verbose_name_plural': 'Contatos'},
        ),
    ]
