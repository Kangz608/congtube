from django.db.models.signals import pre_save
from django.dispatch import receiver

from reviews.models import Review


@receiver(pre_save, sender=Review)
def pre_save_review(sender, instance, **kwargs):
    if instance.order:
        instance.product = instance.order.product

    if instance.product:
        instance.channel = instance.product.channel
