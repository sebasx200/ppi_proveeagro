from django.urls import path
from . import views

# URL configuration for dashboard app.

urlpatterns = [
    path('suppliers/', views.suppliers_list, name='suppliers_list'),
    path('suppliers/add/', views.supplier_add, name='supplier_add'),
]