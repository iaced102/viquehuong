from typing import cast
from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()



class Order(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount      = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.product.name


class Cart(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    cart        = models.ManyToManyField(Order)
    amount      = models.PositiveIntegerField(default=0)
    total_amout = models.PositiveIntegerField(default=0)
    status      = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)

class History_Cart(models.Model):
    carts   = models.ManyToManyField(Cart)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user


class Active_Order(models.Model):
    list_order      = models.ManyToManyField(Order)
    address         = models.CharField(max_length=250)
    customer_name   = models.CharField(max_length=30)
    phone_number    = models.CharField(max_length=15)
    total_price    = models.CharField(max_length=30, blank=True)
    note        = models.TextField(blank=True)