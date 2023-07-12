from django.db import models
from products.models import Product
from core.models import BaseModel


class Order(BaseModel):
    class OrderStatus(models.TextChoices):
        Delivered = ('d', 'delivered')
        Pending = ('p', 'Pending')
        Cooking = ('c', 'cooking')
    products = models.ManyToManyField(Product, through='Product_Order')
    status = models.CharField(max_length=1, choices=OrderStatus.choices, default=OrderStatus.Pending)
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.id)


class Product_Order(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    number = models.IntegerField()
    price = models.PositiveBigIntegerField()


class table(BaseModel):
    table_number = models.IntegerField()
    cafe_space_position = models.CharField(max_length=250)


class Receipt(BaseModel):
    orders = models.ForeignKey(Order, on_delete=models.PROTECT)
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    final_price = models.DecimalField(decimal_places=2, max_digits=8)