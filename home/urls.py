from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search_product', views.SearchProduct.as_view(), name='search_product'),
]