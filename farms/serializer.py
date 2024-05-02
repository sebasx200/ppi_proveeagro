from rest_framework import serializers
from .models import Farm, Farm_Type, CropOrLivestock_Type, CropOrLivestock

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'