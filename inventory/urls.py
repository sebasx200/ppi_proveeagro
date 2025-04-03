from django.urls import path, include
from rest_framework import routers
from . import views

# URL configuration for the inventory app

router = routers.DefaultRouter()
router.register(r"supply_category", views.SupplyCategoryView, "supply_category")
router.register(r"categories", views.CategoryView, "categories")

urlpatterns = [
    path("inventory/", include(router.urls)),
]
