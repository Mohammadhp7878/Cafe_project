from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from .models import User

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
                return redirect('login.html')
        return render(request, self.template)

