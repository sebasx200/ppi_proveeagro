from django.db import models
from suppliers.models import Location

# Create your models here.

class Farm(models.Model):
    """
    this class is used to create a new table for farms in the database with the following fields
    """
    name = models.CharField(max_length=100, verbose_name='Nombre de la finca')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado en')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado en')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Usuario')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Ubicación')
    farm_type = models.ForeignKey('Farm_Type', on_delete=models.CASCADE, verbose_name='Tipo de finca')

    class Meta:
        verbose_name = 'Finca'
        verbose_name_plural = 'Fincas'
        ordering = ['name']

    def __str__(self):
        return self.name

class Farm_Type(models.Model):
    """
    this class is used to create a new table in the database for farm types with the following fields
    """
    name = models.CharField(max_length=100, verbose_name='Tipo de finca')

    class Meta:
        verbose_name = 'Tipo de finca'
        verbose_name_plural = 'Tipos de finca'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class CropOrLivestock_Type(models.Model):
    """
    this class is used to create a new table in the database for crops or livestock types with the following fields
    """
    name = models.CharField(max_length=100, verbose_name='Ganado o Cultivo')
    farm_type = models.ForeignKey(Farm_Type, on_delete=models.CASCADE, verbose_name='Tipo de finca')

    class Meta:
        verbose_name = 'Ganado o Cultivo'
        verbose_name_plural = 'Ganados o Cultivos'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class CropOrLivestock(models.Model):
    """
    this class is used to create a new table in the database for crops or livestock with the following fields
    """
    name = models.CharField(max_length=100, verbose_name='Variedad de cultivo o ganado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado en')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado en')
    crop_or_livestock_type = models.ForeignKey(CropOrLivestock_Type, on_delete=models.CASCADE, verbose_name='Ganado o Cultivo')

    class Meta:
        verbose_name = 'Variedad de cultivo o ganado'
        verbose_name_plural = 'Variedades de cultivo o ganado'
        ordering = ['name']

    def __str__(self):
        return self.name