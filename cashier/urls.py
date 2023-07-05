from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('create_order/', views.CreateOrderView.as_view(), name='order_create'),
    path('product/', views.ProductView.as_view(), name='product'),
    path('total_order', views.TotalOrder.as_view() , name='total_order')
]