# Generated by Django 5.0.4 on 2024-05-24 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0006_alter_farm_options_alter_farm_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_activity', models.CharField(max_length=255, verbose_name='Nombre de la actividad')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
                'ordering': ['name_activity'],
            },
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_type', models.CharField(max_length=255, verbose_name='Nombre del tipo de actividad')),
            ],
            options={
                'verbose_name': 'Tipo de actividad',
                'verbose_name_plural': 'Tipos de actividad',
                'ordering': ['name_type'],
            },
        ),
        migrations.RemoveField(
            model_name='croporlivestock_type',
            name='farm_type',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='farm_type',
        ),
        migrations.AlterField(
            model_name='farm',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nombre de la finca'),
        ),
        migrations.CreateModel(
            name='ActivityDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_description', models.CharField(max_length=255, verbose_name='Descripción de la actividad')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.activity', verbose_name='Actividad')),
            ],
            options={
                'verbose_name': 'Detalle de la actividad',
                'verbose_name_plural': 'Detalles de la actividad',
                'ordering': ['activity_description'],
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.activitytype', verbose_name='Tipo de actividad'),
        ),
        migrations.CreateModel(
            name='FarmActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.activity', verbose_name='Actividad')),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.farm', verbose_name='Finca')),
            ],
            options={
                'verbose_name': 'Actividad de la finca',
                'verbose_name_plural': 'Actividades de la finca',
                'ordering': ['farm'],
                'unique_together': {('farm', 'activity')},
            },
        ),
        migrations.DeleteModel(
            name='CropOrLivestock',
        ),
        migrations.DeleteModel(
            name='CropOrLivestock_Type',
        ),
        migrations.DeleteModel(
            name='Farm_Type',
        ),
    ]