from django.db import models

# Create your models here.

class Supplier(models.Model):

    """
    this class is used to create a new table for suppliers in the database with the following fields
    """

    name = models.CharField(max_length=250, verbose_name='Nombre del Proveedor')
    email = models.EmailField(max_length=250, verbose_name='Dirección de Correo Electrónico', null=True, blank=True)
    phone = models.CharField(max_length=250, verbose_name='Número de Teléfono', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado en')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado en')
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='supplier_created_by', verbose_name='Creado por')
    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='supplier_location', verbose_name='Ubicación')
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Department(models.Model):
    """
    this class is used to create a new table in the database for departments with the following fields
    """
    name = models.CharField(max_length=250, verbose_name='Nombre del Departamento')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class City(models.Model):
    """
    this class is used to create a new table in the database for cities with the following fields
    """
    name = models.CharField(max_length=250, verbose_name='Nombre de la Ciudad')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='city_department', verbose_name='Departamento')

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['name']

    def __str__(self):
        return self.name

class Location(models.Model):
    """
    this class is used to create a new table in the database for locations with the following fields
    """
    address = models.CharField(max_length=250, verbose_name='Dirección')
    latitude = models.FloatField(verbose_name='Latitude', null=True, blank=True)
    longitude = models.FloatField(verbose_name='Longitude', null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='location_city', verbose_name='Ciudad')
    
    class Meta:
        verbose_name = 'Ubicación'
        verbose_name_plural = 'Ubicaciones'
        ordering = ['address']

    def __str__(self):
        return self.address
