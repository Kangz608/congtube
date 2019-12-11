from django.db import models


class BannerManager(models.Manager):

    def is_display(self):
        return self.get_queryset().filter(is_display=True)


def _banner_image_upload_to(banner, filename):
    return 'banners/{filename}'.format(
        filename=filename,
    )


class Banner(models.Model):

    objects = BannerManager()

    image = models.ImageField(
        upload_to=_banner_image_upload_to,
        verbose_name='이미지',
    )
    title = models.CharField(
        max_length=1024,
        verbose_name='이름',
    )
    url = models.URLField(
        verbose_name='URL',
    )

    is_display = models.BooleanField(
        blank=True,
        default=True,
        verbose_name="노출",
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
        verbose_name = '배너'
        verbose_name_plural = '배너'

    def __str__(self):
        return self.title
