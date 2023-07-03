from django.urls import path
from .views import CashierLogin

urlpatterns = [
    path('cahierlogin/', CashierLogin.as_view(), name='cashielogin')
]