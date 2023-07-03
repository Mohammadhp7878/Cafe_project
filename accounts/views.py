from django.shortcuts import render
from django.views import View
from .forms import LoginForm

class CashierLogin(View):
    loginform = LoginForm
    template = 'login.html'

    def get(self, request):
        form = self.loginform(request)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.loginform(request, data=request.POST)
        if form.is_valid():
            ...
        return render(request, self.template)

