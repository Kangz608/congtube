from django.db import models
from channels.models import Channel


class Celebrity(models.Model): # 추후에 User를 추가해야 합니다.
    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    phonenumber = models.CharField(
        null=True,
        blank=True,
        max_length=11
    )

    class Meta:
        verbose_name = '셀럽'
        verbose_name_plural = '셀럽'

    def __str__(self):
        return '채널명 : ' + str(self.channel)
