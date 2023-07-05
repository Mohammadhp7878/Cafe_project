from django.shortcuts import render
from . import models


def home(request):
    about_us = models.AboutUs.objects.order_by('-id').first()
    return render(request, 'base.html', {'about_us': about_us})
