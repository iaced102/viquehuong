from math import ceil
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from order.models import Active_Order
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

# Create your views here.


class Control_Cart(UserPassesTestMixin, TemplateView):
    template_name = 'apps/control_cart.html'
    def get_context_data(self,*args, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['active_order'] = Active_Order.objects.filter(status = False)[0:10]
        context['count_page'] = ceil(len(Active_Order.objects.filter(status = False))/10)
        return context

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        

class Choice_Page(TemplateView):
    template_name = 'apps/list_cart.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_order"] = Active_Order.objects.filter(status = False)[int(self.request.GET['count'])*10-10:int(self.request.GET['count'])*10]
        return context
    

class Detail_Control_Cart(DetailView):
    model = Active_Order
    template_name = 'apps/detail_control_cart.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context