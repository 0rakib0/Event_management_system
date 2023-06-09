from django.urls import path
from . import views
app_name = 'Login'

urlpatterns = [
    path('register/', views.User_register, name='register'),
    path('login/', views.User_login, name='login'),
    path('profile/', views.Profile, name='profile'),
    path('logout/', views.User_logout, name='logout'),
]
