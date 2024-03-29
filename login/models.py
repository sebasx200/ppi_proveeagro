from django import forms
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class CreateNewUser(forms.ModelForm):
    """
    this class is used to create a new user in the database with the following fields
    """
    class Meta:
        model = User
        fields = ['username', 'password', 'password', 'email', 'first_name', 'last_name']

class Supplier(models.Model):
    """
    this class is used to create a new supplier in the database with the following fields
    """
    name = models.CharField(max_length=250, verbose_name='Supplier Name')
    address = models.CharField(max_length=250, verbose_name='Supplier Address')
    latitude = models.FloatField(verbose_name='Latitude', blank=True, null=True)
    longitude = models.FloatField(verbose_name='Longitude', blank=True, null=True)

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        ordering = ['name']

    def __str__(self):
        return self.name