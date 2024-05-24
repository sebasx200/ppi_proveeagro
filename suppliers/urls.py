from django.urls import path, include
from rest_framework import routers
from . import views

# URL configuration for dashboard app.

router = routers.DefaultRouter()
router.register(r'suppliers', views.SupplierView, 'suppliers')
router.register(r'locations', views.LocationView, 'locations')
router.register(r'cities', views.CityView, 'cities')
router.register(r'departments', views.DepartmentView, 'departments')

urlpatterns = [
    path('location/', include(router.urls)),
    path('location/city/', include(router.urls)),
    path('location/department/', include(router.urls)),
    path('supplier/', include(router.urls)),

]