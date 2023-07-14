from django.db.models import Sum
from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models

from django.views.generic import ListView
from products.models import Product

from cafe import settings
from .forms import ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
import logging

logger = logging.getLogger(__name__)


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['text']
            subject = 'contact us,'
            message = f'{name} ** {email} ** {message}'
            email_from = settings.EMAIL_HOST_USER
            try:
                send_mail(subject,message,email_from,["cafeshopproject098@gmail.com"],fail_silently=False,)
                logger.info(f'{name} email received')
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
        else:
            print('form not valid...')
            logger.error('email form not valid...')
    else:
        form = ContactForm()
    about_us = models.AboutUs.objects.order_by('-id').first()
    return render(request, 'base.html', {'about_us': about_us})


class SearchProduct(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'products'

    

    def get_queryset(self):
        search_products = self.request.GET.get('search_product')
        logger.info(f'{search_products} searched')
        if search_products:
            products = Product.objects.filter(name__icontains = search_products)
            return products