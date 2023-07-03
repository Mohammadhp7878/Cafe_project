
from django.views import View
from django.shortcuts import render, redirect
from ..orders.models import Order
from .forms import LoginForm, OrderForm
from .models import User
from django.contrib import messages


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


class CashierLogin(View):
    loginform = LoginForm
    template = 'login.html'

    def get(self, request):
        form = self.loginform(request)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.loginform(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            get_user = User.objects.get(username=username, password=password)
            if get_user:
                return redirect('cashierpanel.html')
            else: 
                return messages.error(request, 'invalid username or password')
        return render(request, self.template, {'form': form})


class CreateOrderView(View):
    def get(self, request):
        form = OrderForm()
        context = {'form': form}
        return render(request, 'order_create.html', context)

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        context = {'form': form}
        return render(request, 'order_create.html', context)

