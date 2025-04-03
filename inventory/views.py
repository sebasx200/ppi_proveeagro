from .models import Supply, Category
from .serializer import CategorySerializer, SupplySerializer, DetailSupplySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

# Create your views here.


class SupplyCategoryView(viewsets.ModelViewSet):
    """
    this is the view to see the supplies with its related category
    """

    serializer_class = SupplySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Supply.objects.all()
        return queryset

    def get_serializer_class(self):
        # detailed serializer for GET requests
        if self.request.method in ["GET", "HEAD", "OPTIONS"]:
            return DetailSupplySerializer
        # simple serializer for other requests
        return SupplySerializer


class CategoryView(viewsets.ReadOnlyModelViewSet):
    """
    this view shows all the categories available
    """

    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
