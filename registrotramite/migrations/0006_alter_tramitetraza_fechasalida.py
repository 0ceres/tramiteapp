# Generated by Django 5.0.7 on 2024-07-25 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrotramite', '0005_alter_tramitetraza_fechasalida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tramitetraza',
            name='fechaSalida',
            field=models.DateTimeField(blank=True),
        ),
    ]
