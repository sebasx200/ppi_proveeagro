from django.urls import path, include
from rest_framework import routers
from . import views

# URL configuration for the login app

router = routers.DefaultRouter()
router.register(r"farms", views.FarmView, "farms")
router.register(r"activity_types", views.ActivityTypeView, "activity_types")
router.register(r"activities", views.ActivityView, "activities")
router.register(r"activity_details", views.ActivityDetailView, "activity_details")
router.register(r"farm_activities", views.FarmActivityView, "farm_activities")
router.register(r"farm_suppliers", views.FarmSupplierView, "farm_suppliers")
router.register(r"farm_supplier_relation", views.FarmSupplierRelationView, "farm_supplier_relation")


urlpatterns = [
    path("farm/", include(router.urls)),
]
