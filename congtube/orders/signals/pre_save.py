from django.db.models.signals import pre_save
from django.dispatch import receiver

from orders.models import Order


@receiver(pre_save, sender=Order)
def pre_save_order(sender, instance, **kwargs):
    if instance.product:
        instance.channel = instance.product.channel
