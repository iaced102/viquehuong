from django.urls import path
from .views import Control_Cart, Choice_Page

urlpatterns = [
    path('control_cart', Control_Cart.as_view(), name ='control_cart'),
    path('choice_page', Choice_Page.as_view(), name='choice_page')
]