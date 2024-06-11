from django.contrib import admin
from .models import Farm, ActivityType, Activity, ActivityDetail, FarmActivity, FarmSupplier

# Register your models here.

admin.site.register(Farm)
admin.site.register(ActivityType)
admin.site.register(Activity)
admin.site.register(ActivityDetail)
admin.site.register(FarmActivity)
admin.site.register(FarmSupplier)
