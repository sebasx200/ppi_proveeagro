from django.db import models
from locations.models import Location
from suppliers.models import Supplier

# Create your models here.

class Farm(models.Model):
    """
    this class is used to create a new table for farms in the database with the following fields
    """
    name = models.CharField(max_length=255, verbose_name='Nombre de la granja')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado en')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado en')
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Usuario')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Ubicación')

    class Meta:
        verbose_name = 'Granja'
        verbose_name_plural = 'Granjas'
        ordering = ['name']

    def __str__(self):
        return self.name

class ActivityType(models.Model):
    """
    this class is used to create a new table for activity types in the database with the following fields
    """
    name_type = models.CharField(max_length=255, verbose_name='Nombre del tipo de actividad')

    class Meta:
        verbose_name = 'Tipo de actividad'
        verbose_name_plural = 'Tipos de actividad'
        ordering = ['name_type']

    def __str__(self):
        return self.name_type

class Activity(models.Model):
    """
    this class is used to create a new table for activities in the database with the following fields
    """
    name_activity = models.CharField(max_length=255, verbose_name='Nombre de la actividad')
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE, verbose_name='Tipo de actividad')

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['name_activity']

    def __str__(self):
        return self.name_activity

class ActivityDetail(models.Model):
    """
    this class is used to create a new table for activity details in the database with the following fields
    """
    activity_description = models.CharField(max_length=255, verbose_name='Descripción de la actividad')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='Actividad')

    class Meta:
        verbose_name = 'Detalle de la actividad'
        verbose_name_plural = 'Detalles de la actividad'
        ordering = ['activity_description']

    def __str__(self):
        return self.activity_description

class FarmActivity(models.Model):
    """
    this class is used to create a new table for farm activities in the database with the following fields
    """
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, verbose_name='Granja')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='Actividad')

    class Meta:
        verbose_name = 'Actividad de la granja'
        verbose_name_plural = 'Actividades de la granja'
        unique_together = ('farm', 'activity')
        ordering = ['farm']

    def __str__(self):
        return f"{self.farm} - {self.activity}" 

class FarmSupplier(models.Model):
    """
    this class is used to create a new table for farm suppliers in the database with the following fields
    """
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, verbose_name='Granja')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Proveedor')

    class Meta:
        verbose_name = 'Proveedor de la granja'
        verbose_name_plural = 'Proveedores de la granja'
        unique_together = ('farm', 'supplier')
        ordering = ['farm']

    def __str__(self):
        return f"{self.farm} - {self.supplier}" 


class AgendaCount(models.Model):
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE)
    agenda_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.supplier.name}: {self.agenda_count} citas"
