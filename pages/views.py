from django.shortcuts import render
from django.views.generic.base import TemplateView
from order.models import Active_Order
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

# Create your views here.


class Control_Cart(UserPassesTestMixin, TemplateView):
    template_name = 'apps/control_cart.html'
    def get_context_data(self,*args, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['active_order'] = Active_Order.objects.filter(status = False)
        return context

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        