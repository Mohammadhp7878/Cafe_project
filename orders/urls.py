from django.urls import path
from . import views
from .views import RemoveFromCartView

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart_view'),
    path('cart/remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
]