from django.urls import path
from .views import DashboardView, CreateOrderView, ProductView


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create_order/', CreateOrderView.as_view(), name='order_create'),
    path('product/', ProductView.as_view(), name='product')
]