# Generated by Django 4.2.1 on 2023-05-30 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criarUsuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='eol',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idade',
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='numero_cadastro',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='numero_certidao',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]