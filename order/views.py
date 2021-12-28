from django.shortcuts import redirect, render
from django.urls import reverse
from products.models import Product
from .models import Order, Cart, Active_Order, Non_Active_Order
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()



def buy_product(request, product, amount):
    context = {}
    context['product'] = Product.objects.get(id=product)
    context['amount'] = amount
    if request.user.is_authenticated:
        get_cart = Q(user__username = request.user.username)
        context['cart'] = Cart.objects.get(get_cart)
    return render(request, 'apps/buy_product.html', context= context)



def active_buy_product(request):
    if request.method == "POST":
        if ',' not in request.POST['product']:
            product = Product.objects.get(id = int(request.POST['product']))
            order = Order.objects.create(product=product, amount = int(request.POST['amount']))
            active_cart = Active_Order.objects.create(address= request.POST['address'], customer_name=request.POST['customer_name'], phone_number=request.POST['phone_number'], total_price=order.product.price*order.amount, note= request.POST['note'])
            active_cart.list_order.add(order)
            active_cart.save()
            return HttpResponse('success')

class Open_Cart(TemplateView):
    template_name='apps/cart.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            get_cart = Q(user__username = self.request.user.username)
            context['cart'] = Cart.objects.get(get_cart)
        return context

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            list_order = self.request.POST['order'].split(',')
            Non_Active_Order.objects.filter(user = self.request.user).delete()
            cart = Non_Active_Order.objects.create(user= self.request.user)
            for order in list_order:
                cart.cart.add(Order.objects.get(id= int(order)))
                cart.save()
            return HttpResponse(cart.id)
    


def change_order(request):
    if request.method == 'POST':
        order = Order.objects.get(id=request.POST['id_order'])
        order.amount= int(request.POST['new_amount'])
        order.save()
        return HttpResponse("success")

def delete_order(request):
    if request.method == "POST":
        Order.objects.get(id=request.POST['id_order']).delete()
        return HttpResponse("success")


def cart(request, cart):
    print(cart)
    context = {}
    context['cart'] = Non_Active_Order.objects.get(user= request.user)
    return render(request,template_name='apps/non_cart.html', context=context)