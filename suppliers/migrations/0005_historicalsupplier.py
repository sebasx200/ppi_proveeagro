# Generated by Django 5.1 on 2024-10-10 03:24

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_historicallocation'),
        ('suppliers', '0004_remove_city_department_remove_location_city_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSupplier',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre del Proveedor')),
                ('email', models.EmailField(blank=True, max_length=250, null=True, verbose_name='Dirección de Correo Electrónico')),
                ('phone', models.CharField(blank=True, max_length=250, null=True, verbose_name='Número de Teléfono')),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='Creado en')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='Actualizado en')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='locations.location', verbose_name='Ubicación')),
            ],
            options={
                'verbose_name': 'historical Proveedor',
                'verbose_name_plural': 'historical Proveedores',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]