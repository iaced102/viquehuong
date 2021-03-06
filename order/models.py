from email.policy import default
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
    user        = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cart        = models.ManyToManyField(Order)
    amount      = models.PositiveIntegerField(default=0)
    total_amout = models.PositiveIntegerField(default=0)
    def __str__(self):
        return str(self.user)


class History_Cart(models.Model):
    carts   = models.ManyToManyField(Cart)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user


class Non_Active_Order(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    cart        = models.ManyToManyField(Order)
    amount      = models.PositiveIntegerField(default=0)
    total_amout = models.PositiveIntegerField(default=0)
    def __str__(self):
        return str(self.user)


class Active_Order(models.Model):
    status          = models.BooleanField(default = False)
    list_order      = models.ManyToManyField(Order)
    address         = models.CharField(max_length=250)
    customer_name   = models.CharField(max_length=30)
    phone_number    = models.CharField(max_length=15)
    total           = models.IntegerField(default=0)
    total_price    = models.CharField(max_length=30, blank=True)
    note        = models.TextField(blank=True)
    def __str__(self):
        return self.customer_name