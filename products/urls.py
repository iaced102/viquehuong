from django.urls import path
from .views import Detail_Product, add_to_cart, List_Products, delete_from_cart

urlpatterns = [
    path('',List_Products.as_view(), name='home'),
    path('detail/<pk>', Detail_Product.as_view(), name='detail_product'),
    path('add_to_cart',add_to_cart, name='add_to_cart'),
    path("delete_from_cart", delete_from_cart, name="delete_from_cart")
]