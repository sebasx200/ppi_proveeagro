# Generated by Django 5.0.2 on 2024-04-29 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0004_remove_farm_farm_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropOrLivestock_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ganado o Cultivo')),
            ],
            options={
                'verbose_name': 'Ganado o Cultivo',
                'verbose_name_plural': 'Ganados o Cultivos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Farm_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tipo de finca')),
            ],
            options={
                'verbose_name': 'Tipo de finca',
                'verbose_name_plural': 'Tipos de finca',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CropOrLivestock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Variedad de cultivo o ganado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado en')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado en')),
                ('crop_or_livestock_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.croporlivestock_type', verbose_name='Ganado o Cultivo')),
            ],
            options={
                'verbose_name': 'Variedad de cultivo o ganado',
                'verbose_name_plural': 'Variedades de cultivo o ganado',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='croporlivestock_type',
            name='farm_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.farm_type', verbose_name='Tipo de finca'),
        ),
        migrations.AddField(
            model_name='farm',
            name='farm_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='farms.farm_type', verbose_name='Farm Type'),
            preserve_default=False,
        ),
    ]
