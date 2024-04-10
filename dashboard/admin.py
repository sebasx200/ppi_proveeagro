from django.contrib import admin
from .models import Supplier, Department, City, Location

# Register your models here.

admin.site.register(Supplier)
admin.site.register(Department)
admin.site.register(City)
admin.site.register(Location)