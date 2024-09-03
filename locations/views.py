from django.shortcuts import render
from locations.models import City, Department, Location
from locations.serializer import CitySerializer, DepartmentSerializer, LocationSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


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
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()


class DepartmentView(viewsets.ReadOnlyModelViewSet):
    """
    this class is used to get the list of departments
    """

    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Department.objects.all()
