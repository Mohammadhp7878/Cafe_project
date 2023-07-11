from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.utils.http import urlencode
from django.conf import settings
from .models import Product

class CartView(View):
    def get(self, request):
        cart_product = request.COOKIES.get('cart')
        number_of_product = {}
        for i in cart_product:
            if i in number_of_product:
                number_of_product[i] += 1
            else:
                number_of_product[i] = int(1)
        number_of_product.pop(',')
        for key in number_of_product.keys():
            products = Product.objects.filter(id=int(key))
        return render(request, 'cart_page.html')

class RemoveFromCartView(View):
    def post(self, request, product_id):
        cart_items = CartView.get_cart_items(request)

        for i, item in enumerate(cart_items):
            if item['id'] == product_id:
                del cart_items[i]
                break

        response = HttpResponse()
        response = CartView.set_cart_items(response, cart_items)

        return response
