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
    permission_classes = [AllowAny]
    def get_queryset(self):
        # Suppliers created by any superuser
        suppliers_by_superusers = Supplier.objects.filter(created_by__is_superuser=True)
        
        # Suppliers created by the current user
        suppliers_by_current_user = Supplier.objects.filter(created_by=self.request.user)
        
        queryset = suppliers_by_superusers | suppliers_by_current_user
        
        return queryset.distinct()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
