# Generated by Django 5.1 on 2024-10-08 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0012_agendacount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendacount',
            old_name='appointment_count',
            new_name='agenda_count',
        ),
    ]