from django.urls import path, include
from rest_framework import routers
from . import views

# URL configuration for the login app

router = routers.DefaultRouter()
router.register(r'farms', views.FarmView, 'farms')

urlpatterns = [
    path('farm/', include(router.urls)),
    path('farm/list', views.farm_list, name='farm_list'),
    path('farm/detail/<int:farm_id>', views.farm_detail, name='farm_detail'),
    path('farm/add', views.farm_add, name='farm_add'),
]