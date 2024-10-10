from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from farms.models import Farm
from suppliers.models import Supplier
from .serializer import FarmHistorySerializer, SupplierHistorySerializer
# Create your views here.

class RecentActionHistoryView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        farms = Farm.objects.filter(created_by=user.id)
        suppliers = Supplier.objects.filter(created_by=user.id)
        return {"farms": farms, "suppliers": suppliers.distinct()}
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        farms = queryset["farms"]
        suppliers = queryset["suppliers"]

        farm_serializer = FarmHistorySerializer(farms, many=True)
        supplier_serializer = SupplierHistorySerializer(suppliers, many=True)

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