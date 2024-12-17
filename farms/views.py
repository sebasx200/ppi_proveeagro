# This file is used to create the views for the farms app
from .models import (
    Farm,
    ActivityType,
    Activity,
    ActivityDetail,
    FarmActivity,
    FarmSupplier,
    AgendaCount,
)
from .serializer import (
    FarmSerializer,
    ActivityTypeSerializer,
    ActivitySerializer,
    ActivityDetailSerializer,
    FarmActivitySerializer,
    FarmSupplierSerializer,
    FarmSupplierRelationSerializer,
)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


class FarmView(viewsets.ModelViewSet):
    """
    this view handles all the Farm model CRUD
    """

    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Farm.objects.filter(created_by=user.id)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
        else:
            print(serializer.errors)


class ActivityTypeView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ActivityTypeSerializer
    permission_classes = [IsAuthenticated]
    queryset = ActivityType.objects.all()


class ActivityView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]
    queryset = Activity.objects.all()


class ActivityDetailView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ActivityDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = ActivityDetail.objects.all()


class FarmActivityView(viewsets.ReadOnlyModelViewSet):
    serializer_class = FarmActivitySerializer
    permission_classes = [IsAuthenticated]
    queryset = FarmActivity.objects.all()


class FarmSupplierView(viewsets.ModelViewSet):
    """
    this is the view that shows the current farm with all its suppliers
    """

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Farm.objects.filter(created_by=user.id)

    def get_serializer_class(self):
        return FarmSupplierSerializer

    def perform_create(self, serializer):
        farm_supplier = serializer.save()

        agenda_count, created = AgendaCount.objects.get_or_create(
            supplier=farm_supplier.supplier
        )
        agenda_count.agenda_count += 1
        agenda_count.save()

        return farm_supplier

    def perform_destroy(self, instance):
        agenda_count = AgendaCount.objects.get(supplier=instance.supplier)
        if agenda_count.agenda_count > 0:
            agenda_count.agenda_count -= 1
            agenda_count.save()
        else:
            agenda_count.agenda_count = 0

        instance.delete()


class FarmSupplierRelationView(viewsets.ModelViewSet):
    """
    this is the view for delete and post request for the FarmSupplier model
    """

    serializer_class = FarmSupplierRelationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FarmSupplier.objects.filter(farm__created_by=user)

    def create(self, request, *args, **kwargs):
        farm_id = request.data.get("farm")
        supplier_id = request.data.get("supplier")

        if FarmSupplier.objects.filter(
            farm_id=farm_id, supplier_id=supplier_id
        ).exists():
            return Response(
                {"detail": "Este proveedor ya fue agendado a la granja"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)
