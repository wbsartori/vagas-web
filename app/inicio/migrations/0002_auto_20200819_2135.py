# Generated by Django 3.1 on 2020-08-20 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fim',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='inicio',
            field=models.CharField(max_length=10),
        ),
    ]