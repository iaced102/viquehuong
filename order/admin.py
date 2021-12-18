from django.contrib import admin
from .models import Order, Cart, History_Cart, Active_Order
# Register your models here.

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(History_Cart)
admin.site.register(Active_Order)