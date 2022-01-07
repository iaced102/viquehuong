from django.contrib import admin
from .models import Non_Active_Order, Order, Cart, History_Cart, Active_Order
# Register your models here.

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(History_Cart)
admin.site.register(Active_Order)
admin.site.register(Non_Active_Order)