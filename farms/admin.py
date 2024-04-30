from django.contrib import admin
from .models import Farm, Farm_Type, CropOrLivestock_Type, CropOrLivestock

# Register your models here.

class FarmAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'farm_type',]
    search_fields = ['name', 'location__address', 'farm_type__name',]
    list_filter = ['location__city__name', 'location__city__department__name', 'farm_type__name',]
    list_per_page = 10

class Farm_TypeAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]
    list_per_page = 10

class CropOrLivestock_TypeAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]
    list_filter = ['name', 'farm_type__name',]
    list_per_page = 10

class CropOrLivestockAdmin(admin.ModelAdmin):
    list_display = ['name', 'crop_or_livestock_type',]
    search_fields = ['name', 'crop_or_livestock_type__name',]
    list_filter = ['crop_or_livestock_type__name',]
    list_per_page = 10

admin.site.register(Farm, FarmAdmin)
admin.site.register(Farm_Type, Farm_TypeAdmin)
admin.site.register(CropOrLivestock_Type, CropOrLivestock_TypeAdmin)
admin.site.register(CropOrLivestock, CropOrLivestockAdmin)
