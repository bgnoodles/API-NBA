# Generated by Django 5.0.6 on 2024-05-21 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0002_jugador'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='posicion',
            field=models.CharField(default='no especificado', max_length=50),
        ),
    ]
