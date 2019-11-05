from django.db import models
from django.contrib.auth import get_user_model

from channels.models import Channel, Product
from orders.models import Order


class ReviewManager(models.Manager):

    def is_display(self):
        return self.get_queryset().filter(is_display=True)

    def is_fake(self):
        return self.get_queryset().filter(is_fake=True)

    def get_rating_mean(self):
        from django.db.models import Avg
        rating_mean = self.get_queryset()\
            .aggregate(rating_mean=Avg("rating"))\
            .get('rating_mean')
        if rating_mean:
            return round(rating_mean, 1)
        return 0


class Review(models.Model):

    objects = ReviewManager()

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
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
        blank=True,
        null=True,
    )

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    RATING_CHOICES = [
        (ONE, ONE),
        (TWO, TWO),
        (THREE, THREE),
        (FOUR, FOUR),
        (FIVE, FIVE),
    ]
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        verbose_name='점수',
    )
    message = models.TextField(
        verbose_name='설명',
    )

    # Custom Review Management System
    is_display = models.BooleanField(
        blank=True,
        default=True,
        verbose_name='표시',
    )
    is_fake = models.BooleanField(
        blank=True,
        default=False,
        verbose_name='가짜',
    )
    fake_name = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name='가짜 이름',
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
        verbose_name = '후기'
        verbose_name_plural = '후기'

        ordering = ['-created_at', ]

    def __str__(self):
        return "({rating}) {message}".format(
            rating=self.rating,
            message=self.message,
        )

    def get_display_name(self):
        if self.is_fake:
            return self.fake_name
        else:
            return self.user.username
    display_name = property(get_display_name)
