from django.urls import path, include
from rest_framework import routers
from .views import FarmList, FarmDelete

# URL configuration for the login app

urlpatterns = [
    path('farm/list/', FarmList.as_view(), name='farm_list'),
    path('farm/delete/<int:pk>/', FarmDelete.as_view(), name='farm_delete'),
    
]