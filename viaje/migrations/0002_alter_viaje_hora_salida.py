# Generated by Django 5.0.3 on 2024-05-12 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viaje', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='hora_salida',
            field=models.TimeField(),
        ),
    ]
