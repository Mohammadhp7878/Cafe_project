from django.views import View
from django.shortcuts import render
from .forms import LoginForm, OrderForm
from .models import User
from django.contrib import messages


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


class DeleteOrderView(View):
    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        return render(request, 'delete.html', {'order': order})

    def post(self, request, pk):
        order = Order.objects.get(id=pk)
        order.delete()
        return redirect('/')

