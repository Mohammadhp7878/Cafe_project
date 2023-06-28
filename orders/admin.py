from django.contrib import admin
from .models import Order , Receipt, table

# Register your models here.
admin.site.register(Order)
admin.site.register(Receipt)
admin.site.register(table)