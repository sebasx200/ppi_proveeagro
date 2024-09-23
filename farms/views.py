# This file is used to create the views for the farms app
from .models import (
    Farm,
    ActivityType,
    Activity,
    ActivityDetail,
    FarmActivity,
    FarmSupplier,
)
from .serializer import (
    FarmSerializer,
    ActivityTypeSerializer,
    ActivitySerializer,
    ActivityDetailSerializer,
    FarmActivitySerializer,
    FarmSupplierSerializer,
    FarmSupplierPostSerializer,
)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


class FarmView(viewsets.ModelViewSet):
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Farm.objects.filter(user=user.id)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
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
    permission_classes = [IsAuthenticated]
    queryset = Farm.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.queryset = FarmSupplier.objects.all()
            return FarmSupplierPostSerializer
        return FarmSupplierSerializer
