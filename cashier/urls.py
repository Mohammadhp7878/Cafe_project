from django.urls import path
from .views import DashboardView, CreateOrderView, ProductView, TotalOrder, DeleteOrderView


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create_order/', CreateOrderView.as_view(), name='order_create'),
    path('product/', ProductView.as_view(), name='product'),
    path('total_order', TotalOrder.as_view(), name='total_order'),
    path('delete_order/<str:pk>', DeleteOrderView.as_view(), name='delete_order')

]