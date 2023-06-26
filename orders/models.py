from django.db import models
from products.models import product

class Order(models.Model):
    products = models.ManyToManyField(through='Product_owner')
    number = models.IntegerField(max_length=5)
    status = models.CharField(max_length=2)
    timestamp = models.DateTimeField()


class Product_owner(models.Model):
    product = models.ForeignKey(product)
    order = models.ForeignKey(Order)