from django.urls import path
from .views import DashboardView, ProductView, TotalOrder, DeleteOrderView, ReceiptView, ChangeStatusView

# app_name = 'cashier'
urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('product/', ProductView.as_view(), name='product'),
    path('total_order', TotalOrder.as_view(), name='total_order'),
    path('delete_order/<str:pk>', DeleteOrderView.as_view(), name='delete_order'),
    path('receipt/<str:pk>', ReceiptView.as_view(), name='receipt'),
    path('change-status/', ChangeStatusView.as_view(), name='change-status'),

]