# Generated by Django 5.1 on 2024-09-03 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0008_farmsupplier'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.location', verbose_name='Ubicación'),
        ),
    ]