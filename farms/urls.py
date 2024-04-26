from django.urls import path
from . import views

# URL configuration for the login app

urlpatterns = [
    path('farm/list', views.farm_list, name='farm_list'),
    path('farm/detail/<int:farm_id>', views.farm_detail, name='farm_detail'),
    path('farm/add', views.farm_add, name='farm_add'),
]