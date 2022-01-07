from django.urls import path

from .views import active_buy_product, buy_product, Open_Cart, change_order, delete_order, cart,active_cart, Open_Cart_When_User_Is_Not_Authenticated

urlpatterns = [
    path('buy/<int:product>/?<int:amount>', buy_product, name="buy"),
    path('active_buy_product', active_buy_product, name='active_buy_product'),
    path('cart', Open_Cart.as_view(), name='cart'),
    path('change_order', change_order, name='change_order'),
    path('delete_order', delete_order, name='delete_order'),
    path('cart/<int:cart>', cart, name='create_cart'),
    path('active_cart',active_cart, name='active_cart'),
    path('get_detail', Open_Cart_When_User_Is_Not_Authenticated.as_view(), name='open_cart_when_user_is_not_authenticated')
]