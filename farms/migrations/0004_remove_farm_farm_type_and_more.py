# Generated by Django 5.0.2 on 2024-04-29 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0003_alter_crop_name_alter_livestock_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm',
            name='farm_type',
        ),
        migrations.RemoveField(
            model_name='livestock',
            name='livestock_type',
        ),
        migrations.DeleteModel(
            name='Crop',
        ),
        migrations.DeleteModel(
            name='Crop_Type',
        ),
        migrations.DeleteModel(
            name='FarmType',
        ),
        migrations.DeleteModel(
            name='Livestock',
        ),
        migrations.DeleteModel(
            name='Livestock_Type',
        ),
    ]
