# This file is used to create the views for the suppliers app
from django.contrib.auth.models import AnonymousUser
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

        if not isinstance(self.request.user, AnonymousUser):
            # Suppliers created by the current user
            suppliers_by_current_user = Supplier.objects.filter(
                created_by=self.request.user
            )

            # both querysets combined
            queryset = suppliers_by_superusers | suppliers_by_current_user
        else:
            queryset = suppliers_by_superusers

        # prefetch_related to include related Supplies
        return queryset.prefetch_related("supplies").distinct()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
