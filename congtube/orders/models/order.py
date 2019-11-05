from django.db import models
from django.contrib.auth import get_user_model

from channels.models import Channel, Product


class OrderManager(models.Manager):

    def is_display(self):
        # 결제실패가 아닌 주문건들에 대해서만 표시한다.
        return self.get_queryset().exclude(status=1)


def _order_video_upload_to(order, filename):
    return 'orders/{filename}'.format(
        filename=filename,
    )


class Order(models.Model):

    objects = OrderManager()

    UNPAID = 1
    PAID = 2
    SUCCESS = 3

    ORDER_STATUS_CHOICES = (
        (UNPAID, '결제실패'),
        (PAID, '결제완료'),
        (SUCCESS, '주문완료'),
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    status = models.PositiveIntegerField(
        choices=ORDER_STATUS_CHOICES,
        default=1,
    )

    merchant_uid = models.CharField(
        max_length=64
    )

    reciever_name = models.CharField(
        max_length=16,
    )

    phonenumber = models.CharField(
        max_length=16,
    )

    email = models.EmailField(
    )

    message = models.TextField(
        max_length=512,
    )

    amount = models.PositiveIntegerField(
        verbose_name='결제 금액',
    )

    video = models.FileField(
        blank=True,
        null=True,
        upload_to=_order_video_upload_to,
        verbose_name='동영상',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='생성일',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='수정일',
    )

    class Meta:
        verbose_name = '주문'
        verbose_name_plural = '주문'

        ordering = ['-created_at', ]

    def __str__(self):
        return '({status}) {product}'.format(
            status=self.get_status_display(),
            product=self.product.name,
        )

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('orders:detail', args=[self.id])
