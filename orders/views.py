from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.utils.http import urlencode
from django.conf import settings
import json

class CartView(View):
    def get_cart_items(self, request):
        cart_items = request.COOKIES.get('cart', None)
        if cart_items:
            cart_items = json.loads(cart_items)
        else:
            cart_items = []
        return cart_items

    def set_cart_items(self, response, cart_items):
        encoded_cart_items = json.dumps(cart_items)
        response.set_cookie('cart', encoded_cart_items, max_age=settings.SESSION_COOKIE_AGE)
        return response

    def get(self, request):
        cart_items = self.get_cart_items(request)

        subtotal = 0.0
        for item in cart_items:
            subtotal += item['price'] * item['quantity']


        context = {
            'cart_items': cart_items,
            'subtotal': subtotal,
        }
        return render(request, 'cart.html', context)

    def post(self, request):
        product_id = request.POST.get('product_id')
        product = {
            'id': product_id,
            'name': 'Sample Product',
            'price': 43.90,
        }

        cart_items = self.get_cart_items(request)

        for item in cart_items:
            if item['id'] == product_id:
                item['quantity'] += 1
                break
        else:
            cart_items.append({
                'id': product['id'],
                'name': product['name'],
                'price': product['price'],
                'quantity': 1,
            })

        response = redirect('cart')
        response = self.set_cart_items(response, cart_items)

        return response

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
