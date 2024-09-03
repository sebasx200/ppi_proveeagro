from django.db import models
from locations.models import Location

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
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='supplier_location', verbose_name='Ubicación')
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['name']

    def __str__(self):
        return self.name
