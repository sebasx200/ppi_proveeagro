# This file is used to create the views for the suppliers app
from .models import Supplier
from .serializer import SupplierSerializer
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
