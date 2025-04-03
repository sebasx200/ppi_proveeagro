from django.db import models
from farms.models import Farm
from suppliers.models import Supplier

# Create your models here.


class Category(models.Model):
    """
    this model is used to represent a supply category
    """

    name = models.CharField(max_length=255, verbose_name="Nombre de la categoría")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado en")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Supply(models.Model):
    """
    this model represents a supply and relates it with a category
    """

    name = models.CharField(max_length=255, verbose_name="Nombre del insumo")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Categoría",
        related_name="supplies",
    )
    farms = models.ManyToManyField(
        Farm, blank=True, verbose_name="Granjas relacionadas", related_name="supplies"
    )
    suppliers = models.ManyToManyField(
        Supplier,
        blank=True,
        verbose_name="Proveedores relacionados",
        related_name="supplies",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado en")

    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"
        ordering = ["name"]

    def __str__(self):
        return self.name
