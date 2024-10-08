from rest_framework import serializers
from locations.models import Location
from locations.serializer import LocationSerializer
from .models import Supplier
from farms.models import AgendaCount


class SupplierSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    is_added_by_superuser = serializers.SerializerMethodField()
    agenda_count = serializers.SerializerMethodField()

    class Meta:
        model = Supplier
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "is_added_by_superuser",
            "created_by",
            "created_at",
            "updated_at",
            "location",
            "agenda_count"
        ]
        extra_kwargs = {"created_by": {"read_only": True}}

    def get_is_added_by_superuser(self, obj):
        return obj.created_by.is_superuser

    def get_agenda_count(self, obj):
        agenda_count = AgendaCount.objects.filter(supplier=obj).first()
        if agenda_count:
            return agenda_count.agenda_count
        return 0

    def create(self, validated_data):
        request = self.context.get("request")
        location_data = validated_data.pop("location")
        location = Location.objects.create(**location_data)
        supplier = Supplier.objects.create(location=location, **validated_data)
        return supplier

    def update(self, instance, validated_data):
        location_data = validated_data.pop("location")
        location = instance.location
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.phone = validated_data.get("phone", instance.phone)
        location.address = location_data.get("address", location.address)
        location.latitude = location_data.get("latitude", location.latitude)
        location.longitude = location_data.get("longitude", location.longitude)
        location.city = location_data.get("city", location.city)
        instance.save()
        location.save()
        return instance
