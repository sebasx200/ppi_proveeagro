# Generated by Django 5.0.2 on 2024-04-01 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_department_city_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='longitude',
        ),
    ]
