# Generated by Django 5.0.3 on 2024-04-05 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_remove_supplier_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='id_department',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='id_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='id_location',
            new_name='location',
        ),
    ]
