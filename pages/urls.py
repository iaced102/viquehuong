from django.urls import path
from .views import Control_Cart

urlpatterns = [
    path('control_cart', Control_Cart.as_view(), name ='control_cart')
]