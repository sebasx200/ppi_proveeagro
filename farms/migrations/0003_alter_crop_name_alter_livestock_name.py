# Generated by Django 5.0.2 on 2024-04-28 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0002_crop_type_livestock_type_crop_livestock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Crop Name'),
        ),
        migrations.AlterField(
            model_name='livestock',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Livestock Name'),
        ),
    ]
