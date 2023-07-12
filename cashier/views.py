from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, redirect
from orders.models import Order, Product_Order, table, Receipt
from products.models import Product
from . import forms
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request):
        status = request.GET.get("status", None)
        orders = Order.objects.all()
        total_order = orders.count()
        deliver = orders.filter(status="d").count()
        pending = orders.filter(status="p").count()
        cooking = orders.filter(status="c").count()
        if status:
            orders = orders.filter(status=status)
        # customer = Customer.objects.all()

        context = {
            "orders": orders,
            # 'customers': customer,
            "total_order": total_order,
            "deliver": deliver,
            "pending": pending,
            "cooking": cooking,
        }
        return render(request, "cashier.html", context)


class ProductView(View):
    def get(self, request):
        items = Product.objects.all()
        return render(request, "inc/products.html", {"items": items})


class ChangeStatusView(View):
    def get(self, request):
        form = forms.StatusForm()
        context = {"form": form}
        return render(request, "inc/dashboard.html", context)

    def post(self, request):
        form = forms.StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard.html")
        context = {"form": form}
        return render(request, "inc/dashboard.html", context)


class DeleteOrderView(View):
    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        return render(request, "inc/delete.html", {"order": order})

    def post(self, request, pk):
        order = Order.objects.get(id=pk)
        if 'confirm' in request.POST:
            order.delete()
            return redirect("dashboard")


class TotalOrder(View):
    def get(self, request):
        content = Order.objects.all()
        return render(request, "inc/totalorder.html", {"content": content})


class FinalRegisterView(View):
    def get(self, request, pk):
        product_order = Product_Order.objects.filter(order_id=pk)
        tables = table.objects.get(id=pk)
        orders = Order.objects.get(id=pk)

        total_price = 0
        total_discount = 0
        total_number = 0

        for product in product_order:
            total_price += product.price * product.number
            total_discount += (product.price * product.product.discount / 100) * product.number
            total_number += product.number

        final_price = total_price - total_discount

        receipt = Receipt.objects.create(orders=orders, total_price=total_price, final_price=final_price)

        return render(request, 'inc/final_register.html',
                      {'product_order': product_order, 'tables': tables, 'orders': orders,
                       'receipt': receipt, 'total_number': total_number, 'total_discount': total_discount})
