from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from .models import Product, Category
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from order.models import Cart, Order
from django.db.models import Q
import json
# Create your views here.





User = get_user_model()


class List_Products(TemplateView):
    template_name = 'list_product.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = Category.objects.all()
        context['products'] = Product.objects.all()

        if self.request.user.is_authenticated:
            get_cart = Q(user__username = self.request.user.username)
            if len(Cart.objects.filter(get_cart))==0:
                Cart.objects.create(user = self.request.user)
            context['cart'] = Cart.objects.filter(get_cart)[0]
        return context
    





class Detail_Product(DetailView):
    model = Product
    template_name = 'detail_product.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_product'] = Product.objects.all()
        if self.request.user.is_authenticated:
            get_cart = Q(user__username = self.request.user.username)
            context['cart'] = Cart.objects.get(get_cart)
        return context


def add_to_cart(request):
    if request.method == 'POST':
        filter_cart = Q(user__id=request.POST['user'])
        cart = Cart.objects.filter(filter_cart)
        if len(cart) == 0:
            new_cart = Cart.objects.create(user = User.objects.get(id=request.POST['user']))         
            new_order = Order.objects.create(product = Product.objects.get(id=request.POST['product']))
            new_cart.cart.add(new_order)
            return HttpResponse('success')
        else:
            list_order = []
            for order in cart[0].cart.all():
                if order.product.id == int(request.POST['product']):
                    list_order.append(order)
            if len(list_order) == 0:
                new_order = Order.objects.create(product = Product.objects.get(id=request.POST['product']))
                cart[0].cart.add(new_order)
                return HttpResponse('sucess')
            else:
                for order in cart[0].cart.all():
                    if order.product.id == int(request.POST['product']):
                        order.amount +=1
                        order.save()
                return HttpResponse("success")



def delete_from_cart(request):
    if request.method == 'POST':
        filter_cart = Q(user__id=request.POST['user'])
        cart = Cart.objects.filter(filter_cart)
        for order in cart[0].cart.all():
            if order.product.id == int(request.POST['id_product']):
                order.delete()
                return HttpResponse("success")


def get_detail(request):
    HttpResponse('sucess')