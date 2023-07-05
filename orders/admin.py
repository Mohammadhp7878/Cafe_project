from django.contrib import admin
from . import models

class Product_OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'order', 'number', 'price']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['status', 'id']
# Register your models here.
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Receipt)
admin.site.register(models.table)
admin.site.register(models.Product_Order, Product_OrderAdmin)