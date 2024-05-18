from django.db import models
from goods.models import Products
from django.contrib.auth.models import User


class Order(models.Model):
    buyer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    operation_id = models.CharField(max_length=100)

class Order_element(models.Model):
    item = models.ForeignKey(Products,on_delete= models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, null = True)
    count = models.IntegerField(default=0, null = True)
    add_date = models.DateTimeField(auto_now_add=True)