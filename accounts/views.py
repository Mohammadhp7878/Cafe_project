from django.views import View
from django.shortcuts import render, redirect
from ..orders.models import Order


class DashboardView(View):
    def get(self, request):
        orders = Order.objects.all()
        # customer = Customer.objects.all()
        total_order = orders.count()
        deliver = orders.filter(status='Delivered').count()
        pending = orders.filter(status='Pending').count()
        cooking = orders.filter(status='Cooking').count()
        send_to_kitchen = orders.filter(status='Sending').count()

        context = {
            'orders': orders,
            # 'customers': customer,
            'total_order': total_order,
            'deliver': deliver,
            'pending': pending,
            'cooking': cooking,
            'send_to_kitchen': send_to_kitchen,
        }
        return render(request, 'dashboard.html', context)



