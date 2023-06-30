from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image_src = models.CharField(max_length=250)
    discount = models.PositiveSmallIntegerField()
    serving_time = models.DurationField()
    estimated_cooking_time = models.DurationField()
    is_available = models.BooleanField(default=True)
    # discount_price = models.PositiveBigIntegerField()

    def discount_to_price(self):
        if self.discount > 0:
            total_price = self.price - (self.price * self.discount / 100)
            return float(total_price)
        return 0

    # def save(self, *args, **kwargs):
    #     self.discount_price = self.discount_to_price()  
    #     super().save(*args, **kwargs)





