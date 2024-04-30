from django.contrib import admin
from .models import Supplier, Department, City, Location

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['id', 'name',]
    list_filter = ['name',]
    list_per_page = 10

class CityAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['id' 'name', 'department__name',]
    list_filter = ['name', 'department__name']
    list_per_page = 10

class LocationAdmin(admin.ModelAdmin):
    list_display = ['address', 'city',]
    search_fields = ['id', 'address', 'city__name',]
    list_filter = ['city__name', 'city__department__name',]
    list_per_page = 10

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'location',]
    search_fields = ['id', 'name', 'phone', 'email', 'location__address']
    list_filter = ['location__city__name', 'location__city__department__name',]
    list_per_page = 10

admin.site.register(Department, DepartmentAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Supplier, SupplierAdmin)