from django.db import models

# Create your models here.

class Supplier(models.Model):

    """
    this class is used to create a new table for suppliers in the database with the following fields
    """

    name = models.CharField(max_length=250, verbose_name='Supplier Name')
    address = models.CharField(max_length=250, verbose_name='Supplier Address')
    latitude = models.FloatField(verbose_name='Latitude', null=True, blank=True)
    longitude = models.FloatField(verbose_name='Longitude', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='supplier_created_by', verbose_name='Created By')
    
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        ordering = ['name']

    def __str__(self):
        return self.name
    
