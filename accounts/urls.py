from django.urls import path
from .views import CashierLogin

urlpatterns = [
    path('cahierpanel/', CashierLogin.as_view())
]