from django.shortcuts import render
from locations.models import City, Department, Location
from locations.serializer import (
    CitySerializer,
    DepartmentSerializer,
    LocationSerializer,
)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny


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
