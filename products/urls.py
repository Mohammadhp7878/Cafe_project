from django.urls import path
from .views import ProductView, SetCooki


urlpatterns = [
    path('product/', ProductView.as_view(), name='new_product'),
    path('category/<slug:category_slug>/', ProductView.as_view(), name='category_filter'),
    path('product/<int:pk>/', SetCooki.as_view(), name='set_cooki'),
]
