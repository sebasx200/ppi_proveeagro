from rest_framework import serializers
from farms.models import Farm, FarmSupplier
from suppliers.models import Supplier

class HistoricalRecordField(serializers.ListField):
    child = serializers.DictField()

    def to_representation(self, data):
        return super().to_representation(data.values())
    
class FarmHistorySerializer(serializers.ModelSerializer):
    history = HistoricalRecordField(read_only=True)
    class Meta:
        model = Farm
        fields = ["id", "name", "created_by", "location", "history"]
        extra_kwargs = {"created_by": {"read_only": True}}

class SupplierHistorySerializer(serializers.ModelSerializer):
    history = HistoricalRecordField(read_only=True)
    class Meta:
        model = Supplier
        fields = ["id", "name", "created_by", "location", "history"]
        extra_kwargs = {"created_by": {"read_only": True}}