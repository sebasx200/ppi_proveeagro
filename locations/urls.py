from django.urls import include, path
from locations import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"locations", views.LocationView, "locations")
router.register(r"cities", views.CityView, "cities")
router.register(r"departments", views.DepartmentView, "departments")


path("location/", include(router.urls)),
path("location/city/", include(router.urls)),
path("location/department/", include(router.urls)),
