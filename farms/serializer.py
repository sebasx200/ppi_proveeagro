from rest_framework import serializers
from .models import Farm, ActivityType, Activity, ActivityDetail, FarmActivity
from suppliers.models import Location
from suppliers.serializer import LocationSerializer

class ActivityTypeSerializer(serializers.ModelSerializer):
        class Meta:
            model = ActivityType
            fields = ['id','name_type']

class ActivitySerializer(serializers.ModelSerializer):
     class Meta:
        model = Activity
        fields = ['id','name_activity','activity_type']

class ActivityDetailSerializer(serializers.ModelSerializer):
     class Meta:
        model = ActivityDetail
        fields = ['id','activity_description','activity']

class FarmActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmActivity
        fields = ['id','farm','activity']

class FarmSerializer(serializers.ModelSerializer):

    location = LocationSerializer()

    class Meta:
        model = Farm
        fields = ['id','name', 'user', 'location']
        extra_kwargs = {'user': {'write_only': True}}

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = Location.objects.create(**location_data)
        farm = Farm.objects.create(location=location, **validated_data)
        return farm
    
    def update(self, instance, validated_data):
        location_data = validated_data.pop('location')
        location = instance.location
        instance.name = validated_data.get('name', instance.name)
        instance.user = validated_data.get('user', instance.user)
        location.address = location_data.get('address', location.address)
        location.city = location_data.get('city', location.city)
        instance.save()
        location.save()
        return instance