# Generated by Django 4.2.1 on 2024-04-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criarUsuario', '0003_alter_usuario_numero_certidao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='e_mail',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
