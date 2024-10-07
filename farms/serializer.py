from rest_framework import serializers
from locations.models import Location
from .models import (
    Farm,
    ActivityType,
    Activity,
    ActivityDetail,
    FarmActivity,
    FarmSupplier,
)
from suppliers.serializer import SupplierSerializer
from locations.serializer import LocationSerializer
from suppliers.models import Supplier


class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = ["id", "name_type"]


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["id", "name_activity", "activity_type"]


class ActivityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityDetail
        fields = ["id", "activity_description", "activity"]


class FarmActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmActivity
        fields = ["id", "farm", "activity"]


class FarmSerializer(serializers.ModelSerializer):
    """
    this serializer handles the farm model and receives the location serializer so it can  be created in the database
    """

    location = LocationSerializer()

    class Meta:
        model = Farm
        fields = ["id", "name", "created_by", "location"]
        extra_kwargs = {"created_by": {"read_only": True}}

    def create(self, validated_data):
        location_data = validated_data.pop("location")
        location = Location.objects.create(**location_data)
        farm = Farm.objects.create(location=location, **validated_data)
        return farm

    def update(self, instance, validated_data):
        location_data = validated_data.pop("location")
        location = instance.location
        instance.name = validated_data.get("name", instance.name)
        location.address = location_data.get("address", location.address)
        location.latitude = location_data.get("latitude", location.latitude)
        location.longitude = location_data.get("longitude", location.longitude)
        location.city = location_data.get("city", location.city)
        instance.save()
        location.save()
        return instance


class FarmSupplierSerializer(serializers.ModelSerializer):
    """
    this is the serializer to get the farms with its related suppliers
    """

    suppliers = serializers.SerializerMethodField()

    class Meta:
        model = Farm
        fields = [
            "id",
            "name",
            "suppliers",
        ]

    def get_suppliers(self, obj):
        # Filtrer the suppliers by current farm
        suppliers = Supplier.objects.filter(farmsupplier__farm=obj)
        return SupplierSerializer(suppliers, many=True).data


class FarmSupplierPostSerializer(serializers.ModelSerializer):
    """
    this serializer relates the farms and the suppliers
    this is the serializer when post request are made
    """

    class Meta:
        model = FarmSupplier
        fields = ["id", "farm", "supplier"]
