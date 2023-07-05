from django.urls import path
from .views import DashboardView, CreateOrderView


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create_order/', CreateOrderView.as_view(), name='order_create')
]