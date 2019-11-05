from django.db import models


class ProductManager(models.Manager):

    def is_display(self):
        return self.get_queryset().filter(is_display=True)


class Product(models.Model):

    objects = ProductManager()

    channel = models.ForeignKey(
        'Channel',
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=64,
        verbose_name='상품명',
    )
    price = models.PositiveIntegerField(
        verbose_name='가격',
    )

    is_display = models.BooleanField(
        blank=True,
        default=True,
        verbose_name='표시',
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
        verbose_name = '상품'
        verbose_name_plural = '상품'

        ordering = ['price', ]

    def __str__(self):
        return "{name}({price})".format(
            name=self.name,
            price=self.price,
        )

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('channels:detail', args=[self.channel.slug])

    def get_cong(self):
        cong = int(self.price) / 110
        return cong
    cong = property(get_cong)
