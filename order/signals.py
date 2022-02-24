from django.db.models.signals import post_save, m2m_changed
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Active_Order


@receiver(m2m_changed, sender=Active_Order.list_order.through)
def m2m_changed_list_order(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove']:
        total = 0
        total_price = 0
        for order in instance.list_order.all():
            total += int(order.amount)
            total_price += int(order.amount) * int(order.product.price)

        instance.total = total
        instance.total_price = total_price
        instance.save()