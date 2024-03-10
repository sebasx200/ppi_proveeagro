from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup, name='signup'), 
    path('home/', views.home, name='home'), 
    path('logout/', views.logout_sesion, name='logout'), 
]