from django.contrib import admin
from .models import Supplier

# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'location',]
    search_fields = ['id', 'name', 'phone', 'email', 'location__address']
    list_filter = ['location__city__name', 'location__city__department__name',]
    list_per_page = 10

admin.site.register(Supplier, SupplierAdmin)