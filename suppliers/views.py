# This file is used to create the views for the suppliers app
from .models import Supplier, Location, City, Department
from .serializer import SupplierSerializer, LocationSerializer, DepartmentSerializer, CitySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
        
class SupplierView(viewsets.ModelViewSet):
    """
    this class is used to create the CRUD views for the suppliers
    """
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Supplier.objects.filter(created_by=user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

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