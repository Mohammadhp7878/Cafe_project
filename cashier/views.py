from typing import Any
from django.views import View
from django.shortcuts import render, redirect
from orders.models import Order
from products.models import Product
from . import forms


class DashboardView(View):
    def get(self, request):
        orders = Order.objects.all()
        # customer = Customer.objects.all()
        total_order = orders.count()
        deliver = orders.filter(status="d").count()
        pending = orders.filter(status="p").count()
        cooking = orders.filter(status="c").count()
        send_to_kitchen = orders.filter(status="s").count()

        context = {
            "orders": orders,
            # 'customers': customer,
            "total_order": total_order,
            "deliver": deliver,
            "pending": pending,
            "cooking": cooking,
            "send_to_kitchen": send_to_kitchen,
        }

        return render(request, 'cashier.html', context)


class ProductView(View):
    def get(self, request):
        items = Product.objects.all()
        return render(request, 'inc/products.html', {'items': items})


class CreateOrderView(View):
    def get(self, request):
        form = forms.OrderForm()
        context = {"form": form}
        return render(request, "inc/order_create.html", context)

    def post(self, request):
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        context = {"form": form}
        return render(request, "inc/order_create.html", context)


class DeleteOrderView(View):
    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        return render(request, "delete.html", {"order": order})

    def post(self, request, pk):
        order = Order.objects.get(id=pk)
        order.delete()
        return redirect("/")
    

class TotalOrder(View):
    def get(self, request):
        content = Order.objects.all()
        return render(request, "inc/totalorder.html", {'content': content})

