from django.db import models

class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField(max_length=20)
    category = ...
    discount = models.PositiveSmallIntegerField(max_length=2)
    serving_time = models.DurationField()
    estimated_cooking_time = models.DurationField()
    