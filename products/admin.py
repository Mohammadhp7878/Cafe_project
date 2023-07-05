from django.contrib import admin
from .models import Product,Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name',]

admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)


