from django.contrib.auth import get_user_model
from django.db import models
from channels.models import Channel


class Celebrity(models.Model):
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
    phonenumber = models.CharField(
        null=True,
        blank=True,
        max_length=11
    )

    def __str__(self):
        return '아이디 : ' + str(self.user) + ', 채널명 : ' + str(self.channel)
