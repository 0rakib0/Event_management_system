from django.urls import path
from . import views

app_name = 'customar'

urlpatterns = [
    path('', views.Home, name='home'),
    path('ticket/<int:price>/', views.Buy_ticket, name='ticket'),
    path('add balance', views.Add_balace, name='add_balance'),
]
