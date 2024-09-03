from locations.models import City, Department, Location
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            "id",
            "name",
        )


class CitySerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = City
        fields = ("id", "name", "department")


class LocationSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Location
        fields = ("id", "address", "latitude", "longitude", "city")

    def to_representation(self, instance):
        self.fields["city"] = CitySerializer()
        return super(LocationSerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        self.fields["city"] = serializers.PrimaryKeyRelatedField(
            queryset=City.objects.all()
        )
        return super(LocationSerializer, self).to_internal_value(data)
