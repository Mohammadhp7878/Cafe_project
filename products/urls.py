from django.urls import path
from .views import ProductView, SessionView


urlpatterns = [
    path('product/', ProductView.as_view(), name='new_product'),
    path('category/<slug:category_slug>/', ProductView.as_view(), name='category_filter'),
]
