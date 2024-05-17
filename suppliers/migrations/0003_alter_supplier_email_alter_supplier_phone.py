# Generated by Django 5.0.4 on 2024-05-17 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_alter_city_options_alter_department_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(blank=True, max_length=250, null=True, verbose_name='Dirección de Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Número de Teléfono'),
        ),
    ]