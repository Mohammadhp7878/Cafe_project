from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    discount = models.PositiveSmallIntegerField(max_length=2)
    serving_time = models.DurationField()
    estimated_cooking_time = models.DurationField()

