from django.urls import path
from .views import active_buy_product, buy_product, Open_Cart, change_order

urlpatterns = [
    path('buy/<int:product>/?<int:amount>', buy_product, name="buy"),
    path('active_cart', active_buy_product, name='active_cart'),
    path('cart', Open_Cart.as_view(), name='cart'),
    path('change_order', change_order, name='change_order')
]