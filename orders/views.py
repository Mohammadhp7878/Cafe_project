from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Order, Product_Order
from products.models import Product

class CartView(View):
    def get(self, request):
        order, created = Order.objects.get_or_create(
            status='OPN',
            timestamp=datetime.now()
        )

        products_in_order = Product_Order.objects.filter(order=order)

        context = {
            'order': order,
            'products_in_order': products_in_order
        }
        return render(request, 'cart.html', context)

    def post(self, request):
        order, created = Order.objects.get_or_create(
            status='OPN',
            timestamp=datetime.now()
        )

        product_id = request.POST.get('product_id')
        action = request.POST.get('action')
        product = Product.objects.get(id=product_id)

        if action == 'add':
            product_order, created = Product_Order.objects.get_or_create(
                product=product,
                order=order
            )
            product_order.number += 1
            product_order.price += product.price
            product_order.save()
            messages.info(request, f"{product.name} has been added to your cart.")

        elif action == 'remove':
            product_order = Product_Order.objects.get(
                product=product,
                order=order
            )
            product_order.number -= 1
            product_order.price -= product.price
            if product_order.number == 0:
                product_order.delete()
                messages.warning(request, f"{product.name} has been removed from your cart.")
            else:
                product_order.save()
                messages.info(request, f"{product.name} quantity has been updated in your cart.")
                
        products_in_order = Product_Order.objects.filter(order=order)

        context = {
            'order': order,
            'products_in_order': products_in_order
        }
        return render(request, 'cart.html', context)