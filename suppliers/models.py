from django.db import models

# Create your models here.

class Supplier(models.Model):

    """
    this class is used to create a new table for suppliers in the database with the following fields
    """

    name = models.CharField(max_length=250, verbose_name='Supplier Name')
    email = models.EmailField(max_length=250, verbose_name='Email Address')
    phone = models.CharField(max_length=250, verbose_name='Phone Number')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='supplier_created_by', verbose_name='Created By')
    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='supplier_location', verbose_name='Location')
    
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Department(models.Model):
    """
    this class is used to create a new table in the database for departments with the following fields
    """
    name = models.CharField(max_length=250, verbose_name='Department Name')

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class City(models.Model):
    """
    this class is used to create a new table in the database for cities with the following fields
    """
    name = models.CharField(max_length=250, verbose_name='City Name')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='city_department', verbose_name='Department')

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['name']

    def __str__(self):
        return self.name

class Location(models.Model):
    """
    this class is used to create a new table in the database for locations with the following fields
    """
    address = models.CharField(max_length=250, verbose_name='Location Address')
    latitude = models.FloatField(verbose_name='Latitude', null=True, blank=True)
    longitude = models.FloatField(verbose_name='Longitude', null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='location_city', verbose_name='City')
    
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        ordering = ['address']

    def __str__(self):
        return self.address
