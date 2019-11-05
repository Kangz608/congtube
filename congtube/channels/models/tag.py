from django.db import models


class Tag(models.Model):

    name = models.CharField(
        max_length=16,
        verbose_name='태그명',
    )
    slug = models.SlugField(
    )

    class Meta:
        verbose_name = '태그'
        verbose_name_plural = '태그'

    def __str__(self):
        return self.name
