from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart_view'),
    path('cart/', views.ReceiptView.as_view(), name='receipt'),
]