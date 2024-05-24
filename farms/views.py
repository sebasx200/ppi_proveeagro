# This file is used to create the views for the farms app
from .models import Farm, Farm_Type
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import FarmSerializer

# Create your views here.

class FarmList(generics.ListCreateAPIView):
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Farm.objects.filter(user=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)

        else:
            print(serializer.errors)

class FarmDelete(generics.DestroyAPIView):
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Farm.objects.filter(user=user)


class FarmView(viewsets.ModelViewSet):
    serializer_class = FarmSerializer
    queryset = Farm.objects.all()