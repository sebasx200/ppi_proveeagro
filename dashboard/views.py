from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from farms.models import Farm, FarmSupplier
from suppliers.models import Supplier
from .serializer import (
    FarmHistorySerializer,
    SupplierHistorySerializer,
    FarmSupplierHistorySerializer,
)

# Create your views here.


class RecentActionHistoryView(viewsets.ReadOnlyModelViewSet):
    """
    this view displays five current actions made by the user in the farm, supplier and farm - supplier models
    """

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        here, we get the data from the historical models and filter it by current user
        """
        user = self.request.user
        farms = Farm.history.filter(created_by=user.id)[:5]
        suppliers = Supplier.history.filter(created_by=user.id)[:5]
        farms_suppliers = FarmSupplier.history.filter(history_user=user.id)[:5]
        return {
            "farms": farms,
            "suppliers": suppliers,
            "farms_suppliers": farms_suppliers,
        }

    def list(self, request, *args, **kwargs):
        """
        this takes the data from the queryset and returns all the data combined
        """
        queryset = self.get_queryset()
        farms = queryset["farms"]
        suppliers = queryset["suppliers"]
        farms_suppliers = queryset["farms_suppliers"]

        # these are the serializers
        farm_serializer = FarmHistorySerializer(farms, many=True)
        supplier_serializer = SupplierHistorySerializer(suppliers, many=True)
        farm_supplier_serializer = FarmSupplierHistorySerializer(
            farms_suppliers, many=True
        )

        # Added type field to each serialized object
        farms_data = farm_serializer.data
        for farm in farms_data:
            farm["type"] = "farm"

        suppliers_data = supplier_serializer.data
        for supplier in suppliers_data:
            supplier["type"] = "supplier"

        farms_suppliers_data = farm_supplier_serializer.data
        for farm_supplier in farms_suppliers_data:
            farm_supplier["type"] = "farm_supplier"

        combined_data = [
            {"farms": farms_data},
            {"suppliers": suppliers_data},
            {"farms_suppliers": farms_suppliers_data},
        ]

        return Response(combined_data, status=status.HTTP_200_OK)
