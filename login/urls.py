from django.urls import path
from . import views

# URL configuration for the login app

urlpatterns = [
    path('', views.main, name='main'),
    path('get_suppliers/', views.get_suppliers, name='get_suppliers'),
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup, name='signup'), 
    path('logout/', views.logout_sesion, name='logout'), 
]