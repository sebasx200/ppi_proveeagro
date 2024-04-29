from django.contrib import admin
from .models import Farm, Farm_Type, CropOrLivestock_Type, CropOrLivestock

# Register your models here.

class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'user', 'location', 'farm_type')
    search_fields = ('name', 'user', 'location', 'farm_type')
    list_filter = ('created_at', 'updated_at', 'user', 'location', 'farm_type')
    list_per_page = 10

class Farm_TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 10

class CropOrLivestock_TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'farm_type')
    search_fields = ('name', 'farm_type')
    list_filter = ('farm_type',)
    list_per_page = 10

class CropOrLivestockAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    list_per_page = 10

admin.site.register(Farm, FarmAdmin)
admin.site.register(Farm_Type, Farm_TypeAdmin)
admin.site.register(CropOrLivestock_Type, CropOrLivestock_TypeAdmin)
admin.site.register(CropOrLivestock, CropOrLivestockAdmin)
