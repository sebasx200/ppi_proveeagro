from django.contrib import admin
from .models import Supplier, Department, City, Location

# Register your models here.


admin.site.register(Department)
admin.site.register(City)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id','address',)
    list_editable = ('address',)
    list_per_page = 10

admin.site.register(Location, LocationAdmin)
    
class SupplierAdmin(admin.ModelAdmin):
    list_display=('Supplier','location','phone')
    ordering=('name',)
    search_fields = ('name',)
    list_per_page = 10

    def Supplier(self,obj):
        return obj.name.upper()

admin.site.register(Supplier, SupplierAdmin)