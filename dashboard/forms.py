from django.forms import ModelForm
from .models import Supplier, Location, City, Department

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name']

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['address', 'latitude', 'longitude']
