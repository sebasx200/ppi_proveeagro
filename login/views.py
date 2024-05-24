#This file contains the views for the login app.
from django.contrib.auth.models import User

# new imports for the API
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import UserSerializer

# Create your views here.

class CreateUserView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]