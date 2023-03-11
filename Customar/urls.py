from django.urls import path
from . import views

app_name = 'customar'

urlpatterns = [
    path('home/', views.Home, name='home')
]
