from django.shortcuts import render
from locations.models import City, Department, Location
from locations.serializer import (
    CitySerializer,
    DepartmentSerializer,
    LocationSerializer,
)
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from farms.serializer import FarmSerializer
from suppliers.serializer import SupplierSerializer
from farms.models import Farm
from suppliers.models import Supplier
from rest_framework.response import Response


# Create your views here.
class LocationView(viewsets.ReadOnlyModelViewSet):
    """
    this class is used to get the list of locations
    """

    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
    queryset = Location.objects.all()


class CityView(viewsets.ReadOnlyModelViewSet):
    """
    this class is used to get the list of cities
    """

    serializer_class = CitySerializer
    permission_classes = [AllowAny]
    queryset = City.objects.all()

    # tbis custom queryset is used when a filter is needed to show only the cities related with the department_id
    def get_queryset(self):
        queryset = super().get_queryset()
        department_id = self.request.query_params.get("department_id", None)

        if department_id:
            queryset = queryset.filter(department_id=department_id)
        return queryset


class DepartmentView(viewsets.ReadOnlyModelViewSet):
    """
    this class is used to get the list of departments
    """

    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Department.objects.all()


class FarmSupplierLocationsView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user

        # Suppliers created by any superuser
        suppliers_by_superusers = Supplier.objects.filter(created_by__is_superuser=True)

        # Suppliers created by the current user
        suppliers_by_current_user = Supplier.objects.filter(created_by=user.id)

        # both supplier querysets combined
        suppliers = suppliers_by_superusers | suppliers_by_current_user

        # Farms created by the current user
        farms = Farm.objects.filter(created_by=user.id)

        # the farms and suppliers are return separately
        return {"farms": farms, "suppliers": suppliers.distinct()}

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        farms = queryset["farms"]
        suppliers = queryset["suppliers"]

        farm_serializer = FarmSerializer(farms, many=True)
        supplier_serializer = SupplierSerializer(suppliers, many=True)

        # Added type field to each serialized object
        farms_data = farm_serializer.data
        for farm in farms_data:
            farm['type'] = 'farm'

        suppliers_data = supplier_serializer.data
        for supplier in suppliers_data:
            supplier['type'] = 'supplier'

        combined_data = [
            {"farms": farms_data},
            {"suppliers": suppliers_data},
        ]

        return Response(combined_data, status=status.HTTP_200_OK)
