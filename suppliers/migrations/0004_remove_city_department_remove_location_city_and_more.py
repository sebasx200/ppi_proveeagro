# Generated by Django 5.1 on 2024-09-03 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0009_alter_farm_location'),
        ('locations', '0001_initial'),
        ('suppliers', '0003_alter_supplier_email_alter_supplier_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='department',
        ),
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_location', to='locations.location', verbose_name='Ubicación'),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
