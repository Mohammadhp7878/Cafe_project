from django.views import View
from django.shortcuts import render, redirect
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


