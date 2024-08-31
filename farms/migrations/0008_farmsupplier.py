# Generated by Django 5.0.4 on 2024-06-11 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0007_activity_activitytype_and_more'),
        ('suppliers', '0003_alter_supplier_email_alter_supplier_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.farm', verbose_name='Finca')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier', verbose_name='Proveedor')),
            ],
            options={
                'verbose_name': 'Proveedor de la finca',
                'verbose_name_plural': 'Proveedores de la finca',
                'ordering': ['farm'],
                'unique_together': {('farm', 'supplier')},
            },
        ),
    ]