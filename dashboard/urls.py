from django.urls import path, include
from rest_framework import routers
from . import views

# URL configuration for dashboard app.

router = routers.DefaultRouter()
router.register(r"action_history", views.RecentActionHistoryView, "action_history")

urlpatterns = [
    path("dashboard/", include(router.urls)),
]