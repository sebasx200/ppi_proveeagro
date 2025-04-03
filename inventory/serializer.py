from rest_framework import serializers
from .models import Category, Supply
from suppliers.serializer import SimpleSupplierSerializer
from farms.serializer import SimpleFarmSerializer


class CategorySerializer(serializers.ModelSerializer):
    """
    this is the Caregory model serializer
    """

    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class SupplySerializer(serializers.ModelSerializer):
    """
    this serializer handles the supplies and its releated objects, it is used for post requests
    """

    class Meta:
        model = Supply
        fields = ["id", "name", "description", "category", "farms", "suppliers"]


class DetailSupplySerializer(serializers.ModelSerializer):
    """
    this is a more detailed serialiazer which represents all the data releated, it is used for get requests
    """

    category = CategorySerializer()
    farms = SimpleFarmSerializer(many=True)
    suppliers = SimpleSupplierSerializer(many=True)

    class Meta:
        model = Supply
        fields = ["name", "description", "category", "farms", "suppliers"]
