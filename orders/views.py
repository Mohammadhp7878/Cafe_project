from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.utils.http import urlencode
from django.conf import settings
from .models import Product
from datetime import datetime, timedelta

class CartView(View):
    def get(self, request):
        cart_product = request.COOKIES.get('cart')
        cart_list = cart_product.split(',') if cart_product else []
        number_of_product = {}

        for key in cart_list:
            if key in number_of_product:
                number_of_product[key] += 1
            else:
                number_of_product[key] = int(1)
        products = []

        for key, value in number_of_product.items():
            try:
                product = Product.objects.get(id=int(key))
                total_price = float(f'{product.discount_to_price * value:.2f}')
                products.append({'product': product, 'quantity': value, 'name': product.name,
                                 'price': product.price, 'category': product.category,
                                 'discount': product.discount, 'total': product.discount_to_price,
                                 'total_price':total_price, 'id':product.id})
                total_price_sum = sum(product['total_price'] for product in products)
            except Product.DoesNotExist:
                pass
        return render(request, 'cart_page.html', {'products': products, 'total_price_sum': f'{total_price_sum:.2f}'})
    

    def post(self, request):

        print(*request)
        return redirect('cart.html')

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

