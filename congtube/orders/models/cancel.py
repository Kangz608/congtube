from django.db import models


class Cancel(models.Model):
    cancelreason = models.CharField(
        max_length=64,
    )

    class Meta:
        verbose_name = '취소사유'
        verbose_name_plural = '취소사유'

    def __str__(self):
        return self.cancelreason