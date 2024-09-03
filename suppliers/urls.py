from django.urls import path, include
from rest_framework import routers
from . import views

# URL configuration for dashboard app.

router = routers.DefaultRouter()
router.register(r'suppliers', views.SupplierView, 'suppliers')

urlpatterns = [
    path('supplier/', include(router.urls)),
]