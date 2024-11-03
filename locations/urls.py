from django.urls import include, path
from locations import views
from rest_framework import routers

# URL configuration for the locations app

router = routers.DefaultRouter()
router.register(r"locations", views.LocationView, "locations")
router.register(r"cities", views.CityView, "cities")
router.register(r"departments", views.DepartmentView, "departments")
router.register(
    r"farm_supplier_locations",
    views.FarmSupplierLocationsView,
    "farm_supplier_locations",
)

urlpatterns = [
    path("location/", include(router.urls)),
]
