from django.views import View
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
import logging

logger = logging.getLogger(__name__)

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
            get_user = authenticate(request, phone_number=username, password=password)
            if get_user:
                login(request, get_user)
                logger.info(f'user {username} login successfully')
                return redirect('dashboard')
            else:
                logger.warning(f'user {username}: invalid username or password')
                return messages.error(request, 'invalid username or password')
        return render(request, self.template, {'form': form})


