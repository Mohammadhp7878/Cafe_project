from django.shortcuts import render
from . import models
from .forms import ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            try:
                send_mail('contact', f'{name}\n{email}\n{number}', email, ["en.moradi.66@gmail.com"],)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
        else:
            print('form not valid...')
    else:
        form = ContactForm()
    about_us = models.AboutUs.objects.order_by('-id').first()
    return render(request, 'base.html', {'about_us': about_us})
