from django.urls import path
from .views import CashierLogin

urlpatterns = [
    path('cashierlogin/', CashierLogin.as_view(), name='cashierlogin')
]