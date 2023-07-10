from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Category
from django.views.generic import ListView, DetailView
from django.contrib.messages import constants as messages


class ProductView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.all()
        categories = Category.objects.all()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category = category)
        return render(request, 'product/new_product.html', {'products': products, 'categories': categories})

class SetCooki(View):
    def get(self, request, pk):
        cart_cookie = request.COOKIES.get('cart')
        cart_list = cart_cookie.split(',') if cart_cookie else []
        cart_list.append(str(pk))
        cart_cookie = ','.join(cart_list)
        response = redirect(request.META.get('HTTP_REFERER'))
        response.set_cookie('cart', cart_cookie)
        print(f'This is the cart cookie: {cart_cookie}')
        return response


        



