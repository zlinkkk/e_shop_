from django.db import models

# Create your models here.
class Products(models.Model):
    class Meta:
        db_table = 'products'

    name = models.CharField(max_length = 100)
    color = models.CharField(max_length = 30)
    buy_price = models.FloatField(max_length = 100000)
    sell_price = models.FloatField(max_length = 100000)
    img_link = models.CharField(max_length = 100)

# class 