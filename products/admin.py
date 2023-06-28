from django.contrib import admin
from .models import Product,Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'discount']
    exclude = ('discount_price',)  

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
