from rest_framework import serializers
from .models import Supplier, Location, City, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name',)

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id','name', 'department')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('address', 'latitude', 'longitude', 'city')

class SupplierSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Supplier
        fields = ['id','name', 'email', 'phone', 'created_at', 'updated_at', 'created_by', 'location']

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = Location.objects.create(**location_data)
        supplier = Supplier.objects.create(location=location, **validated_data)
        return supplier
    
    def update(self, instance, validated_data):
        location_data = validated_data.pop('location')
        location = instance.location
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        location.address = location_data.get('address', location.address)
        location.city = location_data.get('city', location.city)
        instance.save()
        location.save()
        return instance