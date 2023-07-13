from django.contrib import admin
from .models import Product,Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name',]
    exclude = ['slug']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'discount', 'is_available']
    ordering = ['name', 'price']
    list_filter = ['is_available']
    search_fields = ['name', 'price']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


