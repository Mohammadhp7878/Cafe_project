from datetime import datetime
from django.shortcuts import render
from django.contrib import messages
from django.views import View
from django.urls import reverse
from .models import Order, Receipt
from products.models import Product

class CartView(View):
    def get(self, request):
        cart_cookie = request.COOKIES.get('cart')
        print(cart_cookie)
        return render(request, 'cart_page.html')

    def post(self, request):
        order = self.get_order(request)
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')
        product = Product.objects.get(id=product_id)

        if action == 'add':
            order.products.add(product)
            messages.info(request, f"{product.name} has been added to your cart.")

        elif action == 'remove':
            order.products.remove(product)
            messages.warning(request, f"{product.name} has been removed from your cart.")

        products_in_order = order.products.all()
        total_price = self.calculate_total_price(products_in_order)
        receipt = self.create_or_update_receipt(order, total_price)
        context = self.get_context_data(order, products_in_order, receipt)
        return render(request, 'cart.html', context)

    def get_order(self, request):
        order, created = Order.objects.get_or_create(
            status='OPN',
            timestamp=datetime.now()
        )
        return order

    def calculate_total_price(self, products_in_order):
        total_price = sum([product.price for product in products_in_order])
        return total_price

    def create_or_update_receipt(self, order, total_price):
        receipt, created = Receipt.objects.get_or_create(order=order)
        receipt.total_price = total_price
        receipt.final_price = total_price
        receipt.save()
        return receipt

    def get_context_data(self, order, products_in_order, receipt):
        context = {
            'order': order,
            'products_in_order': products_in_order,
            'total_price': receipt.total_price,
            'final_price': receipt.final_price,
            'payment_url': reverse('banking') # assuming a URL pattern named 'banking' exists
        }
        return context