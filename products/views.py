from django.views import View
from django.shortcuts import render
from .models import Product


class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'base.html', {'products': products})

