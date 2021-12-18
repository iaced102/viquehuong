from django.contrib import admin

# Register your models here.

from .models import Category, Product, Description_image



admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Description_image)