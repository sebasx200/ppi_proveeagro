from django.contrib import admin
from .models import (
    Farm,
    ActivityType,
    Activity,
    ActivityDetail,
    FarmActivity,
    FarmSupplier,
)
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

admin.site.register(Farm, SimpleHistoryAdmin)
admin.site.register(ActivityType)
admin.site.register(Activity)
admin.site.register(ActivityDetail)
admin.site.register(FarmActivity)
admin.site.register(FarmSupplier)
