from django.contrib import admin
from .models import Farm, FarmType, Crop_Type, Crop, Livestock_Type, Livestock

# Register your models here.

admin.site.register(Farm)
admin.site.register(FarmType)
admin.site.register(Crop_Type)
admin.site.register(Crop)
admin.site.register(Livestock_Type)
admin.site.register(Livestock)