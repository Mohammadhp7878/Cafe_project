import logging
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.utils.http import urlencode
from django.conf import settings
from .models import Product, Order, Product_Order, Receipt
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

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
                if product.discount:
                    total_price = float(f'{product.discount_to_price * value:.2f}')
                else:
                    total_price = float(f'{product.price * value:.2f}')
                products.append({'product': product, 'quantity': value, 'name': product.name,
                                 'price': product.price, 'category': product.category,
                                 'discount': product.discount, 'total': product.discount_to_price,
                                 'total_price':total_price, 'id':product.id, 'image': product.image_src})
                total_price_sum = sum(product['total_price'] for product in products)
            except Product.DoesNotExist:
                logger.error(f"Product with ID {key} does not exist")
        logger.info(f"Cart view rendered successfully with {len(products)} products")
        return render(request, 'cart_page.html', {'products': products, 'total_price_sum': f'{total_price_sum:.2f}'})


    def post(self, request):

        print(*request)
        return redirect('cart.html')

class ReceiptView(View):
    def get(self, request):
        return render(request, 'inc/receipt.html')
    def post(self, request):
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
            product = Product.objects.get(id=int(key))
            if product.discount:
                total_price = round(product.discount_to_price * value, 2)
            else:
                total_price = round(product.price * value, 2)
            products.append({'quantity': value, 'total': product.discount_to_price,
                             'total_price': total_price, 'id': product.id})
            total_price_sum += total_price

        order = Order.objects.create(status=Order.OrderStatus.Pending)
        order_id = order.id

        for product in products:
            Product_Order.objects.create(product_id=product['id'], order_id=order_id,
                                         number=product['quantity'], price=total_price_sum)

        Receipt.objects.create(order_id=order_id, total_price=total_price_sum, final_price=total_price_sum)

        return render(request, 'inc/receipt.html', {'products': products, 'order_id': order_id})
        
        





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

