from rest_framework import serializers
from farms.models import Farm, FarmSupplier
from suppliers.models import Supplier


class FarmHistorySerializer(serializers.ModelSerializer):
    """
    this is the farm history serializer which takes the farm historical table as model
    """

    history_user = serializers.StringRelatedField()  # to show the user

    class Meta:
        model = Farm.history.model  # this is the historical model of the object
        fields = [
            "id",
            "name",
            "location",
            "history_date",
            "history_user",
            "history_type",
        ]


class SupplierHistorySerializer(serializers.ModelSerializer):
    """
    this is the suppplier history serializer which takes the supplier historical table as model
    """

    history_user = serializers.StringRelatedField()  # # to show the user

    class Meta:
        model = Supplier.history.model  # this is the historical model of the object
        fields = [
            "id",
            "name",
            "location",
            "history_date",
            "history_user",
            "history_type",
        ]


class FarmSupplierHistorySerializer(serializers.ModelSerializer):
    """
    this is the farm - supplier history serializer which takes the farm - supplier historical table as model
    """

    farm_name = serializers.SerializerMethodField()
    supplier_name = serializers.SerializerMethodField()

    class Meta:
        model = FarmSupplier.history.model  # this is the historical model of the object
        fields = [
            "id",
            "farm",
            "farm_name",
            "supplier",
            "supplier_name",
            "history_date",
            "history_user",
            "history_type",
        ]

    # this gets the name of the farm from the objetct
    def get_farm_name(self, obj):
        try:
            return obj.farm.name
        except Farm.DoesNotExist:
            return None

    # this gets the name of the supplier from the objetct
    def get_supplier_name(self, obj):
        try:
            return obj.supplier.name
        except Supplier.DoesNotExist:
            return None
