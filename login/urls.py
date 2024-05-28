from django.urls import path, include

# URL configuration for the login app

from .views import CreateUserView, UserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/user/register/', CreateUserView.as_view(), name='register'),
    path('login/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('login-auth/', include('rest_framework.urls')),
    path('login/user/profile/', UserView.as_view(), name='user_profile'), 
    
]