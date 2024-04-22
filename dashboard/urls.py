from django.urls import path
from . import views

# URL configuration for dashboard app.

urlpatterns = [
    path('home/', views.home, name='home'), 
]