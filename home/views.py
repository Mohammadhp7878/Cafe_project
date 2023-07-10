from django.db.models import Sum
from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models
from django.views.generic import ListView
from products.models import Product

def home(request):
    about_us = models.AboutUs.objects.order_by('-id').first()
    return render(request, 'base.html', {'about_us': about_us})


class SearchProduct(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'products'

    def get_queryset(self):
        search_products = self.request.GET.get('search_product')
        top_selling = top_selling_products = Product.objects.annotate(total_quantity=Sum('product_order__number')).order_by('-total_quantity')[:10]
        if search_products:
            products = Product.objects.filter(name__icontains = search_products)
            return products