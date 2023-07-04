from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Product, Category
from django.contrib.messages import constants as messages


class ProductView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.all()
        categories = Category.objects.all()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category = category)

        return render(request, 'product/new_product.html', {'products': products, 'categories': categories})
    
    


