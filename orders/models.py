from django.db import models
from ..products.models import Product
from ..core.models import BaseModel


class Order(BaseModel):
    products = models.ManyToManyField(Product, through='Product_Order')
    status = models.CharField(max_length=2)
    timestamp = models.DateTimeField()


class Product_Order(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    number = models.IntegerField()
    price = models.PositiveBigIntegerField()


class table(BaseModel):
    table_number = models.IntegerField()
    cafe_space_position = models.CharField(max_length=250)


class Receipt(BaseModel):
    orders = models.ForeignKey(Order, on_delete=models.PROTECT)
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    final_price = models.DecimalField(decimal_places=2, max_digits=8)