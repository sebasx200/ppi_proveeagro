from rest_framework import serializers
from .models import Supplier, Location, City, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name',)

class CitySerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = City
        fields = ('id', 'name', 'department')

class LocationSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Location
        fields = ('address', 'latitude', 'longitude', 'city')

class SupplierSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'email', 'phone', 'created_at', 'updated_at', 'location']
        extra_kwargs = {"created_by": {"read_only": True}}

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        city_data = location_data.pop('city')
        department_data = city_data.pop('department')
        
        department, created = Department.objects.get_or_create(**department_data)
        city, created = City.objects.get_or_create(department=department, **city_data)
        location, created = Location.objects.get_or_create(city=city, **location_data)
        
        supplier = Supplier.objects.create(location=location, **validated_data)
        return supplier
    
    def update(self, instance, validated_data):
        location_data = validated_data.pop('location')
        city_data = location_data.pop('city')
        department_data = city_data.pop('department')
        
        department, created = Department.objects.get_or_create(**department_data)
        city, created = City.objects.get_or_create(department=department, **city_data)
        location, created = Location.objects.get_or_create(city=city, **location_data)
        
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.location = location
        
        instance.save()
        return instance