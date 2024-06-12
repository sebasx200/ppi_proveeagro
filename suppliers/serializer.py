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
        fields = ('id','name', 'department')

class LocationSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Location
        fields = ('id', 'address', 'latitude', 'longitude', 'city')

    def to_representation(self, instance):
        self.fields['city'] = CitySerializer()
        return super(LocationSerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        self.fields['city'] = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
        return super(LocationSerializer, self).to_internal_value(data)

class SupplierSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Supplier
        fields = ['id','name', 'email', 'phone', 'created_at', 'updated_at', 'location']
        extra_kwargs = {"created_by": {"read_only": True}}

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
        location.address = location_data.get('address', location.address)
        location.city = location_data.get('city', location.city)
        instance.save()
        location.save()
        return instance