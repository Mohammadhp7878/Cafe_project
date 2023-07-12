from django.urls import path
from .views import CashierLogin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('cashierlogin/', CashierLogin.as_view(), name='cashierlogin'),
    path('logout/', LogoutView.as_view(), name='logout')
]