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


class SimpleFarmSerializer(serializers.ModelSerializer):
    """
    this serializer works when a simple farm data is needed without all the relation fields
    """

    class Meta:
        model = Farm
        fields = ["id", "name", "created_by"]


class SupplierSerializer(serializers.ModelSerializer):
    """
    this a custom serializer for supplier which brings the relation with the farm from the FarmSupplier model
    """

    relation_id = serializers.SerializerMethodField()

    class Meta:
        model = Supplier
        fields = ["id", "name", "relation_id"]

    def get_relation_id(self, obj):
        # Get the farm from the context
        farm = self.context.get("farm")
        if farm:
            try:
                relation = FarmSupplier.objects.get(farm=farm, supplier=obj)
                return relation.id
            except FarmSupplier.DoesNotExist:
                return None
        return None


class FarmSupplierSerializer(serializers.ModelSerializer):
    """
    this serializer releates the current farm with all the supplier it is related with
    """

    suppliers = serializers.SerializerMethodField()

    class Meta:
        model = Farm
        fields = ["id", "name", "suppliers"]

    def get_suppliers(self, obj):
        # Get the supplier related with the current farm
        suppliers = Supplier.objects.filter(farmsupplier__farm=obj)
        return SupplierSerializer(suppliers, many=True, context={"farm": obj}).data


class FarmSupplierRelationSerializer(serializers.ModelSerializer):
    """
    this serializer relates the farms and the suppliers
    this is the serializer when post request are made
    """

    class Meta:
        model = FarmSupplier
        fields = ["id", "farm", "supplier"]
