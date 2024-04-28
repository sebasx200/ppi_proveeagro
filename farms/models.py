from django.db import models
from suppliers.models import Location

# Create your models here.

class Farm(models.Model):
    """
    this class is used to create a new table for farms in the database with the following fields
    """
    name = models.CharField(max_length=100, verbose_name='Farm Name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='User')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Location')
    farm_type = models.ForeignKey('FarmType', on_delete=models.CASCADE, verbose_name='Farm Type')

    class Meta:
        verbose_name = 'Farm'
        verbose_name_plural = 'Farms'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class FarmType(models.Model):
    """
    this class is used to create a new table in the database for farm types with the following fields
    """
    name = models.CharField(max_length=100, verbose_name='Farm Type')

    class Meta:
        verbose_name = 'Farm Type'
        verbose_name_plural = 'Farm Types'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Crop_Type(models.Model):
    """
    this class is used to create a new table in the database for crop types with the following fields
    """
    name = models.CharField(max_length=100, verbose_name='Crop Type')

    class Meta:
        verbose_name = 'Crop Type'
        verbose_name_plural = 'Crop Types'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Crop(models.Model):
    """
    this class is used to create a new table in the database for crops with the following fields
    """
    name = models.CharField(max_length=100, verbose_name='Crop Name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    crop_type = models.ForeignKey(Crop_Type, on_delete=models.CASCADE, verbose_name='Crop Type')

    class Meta:
        verbose_name = 'Crop'
        verbose_name_plural = 'Crops'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Livestock_Type(models.Model):
    """
    this class is used to create a new table in the database for livestock types with the following fields
    """
    name = models.CharField(max_length=100, verbose_name='Livestock Type')

    class Meta:
        verbose_name = 'Livestock Type'
        verbose_name_plural = 'Livestock Types'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Livestock(models.Model):
    """
    this class is used to create a new table in the database for livestock with the following fields
    """
    name = models.CharField(max_length=100, verbose_name='Livestock Name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    livestock_type = models.ForeignKey(Livestock_Type, on_delete=models.CASCADE, verbose_name='Livestock Type')

    class Meta:
        verbose_name = 'Livestock'
        verbose_name_plural = 'Livestocks'
        ordering = ['name']

    def __str__(self):
        return self.name
