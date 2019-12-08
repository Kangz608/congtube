from django.db import models


class ChannelQuerySet(models.QuerySet):

    def is_display(self):
        return self.filter(is_display=True)

    def is_hot(self):
        return self.filter(is_hot=True)

    def random(self):
        return self.order_by('?')


class ChannelManager(models.Manager):

    def get_queryset(self):
        return ChannelQuerySet(self.model, using=self._db)

    def is_display(self):
        return self.get_queryset().is_display()

    def is_hot(self):
        return self.get_queryset().is_hot()

    def random(self):
        return self.get_queryset().random()


def _channel_image_upload_to(channel, filename):
    extension = filename.split('.')[-1]
    return 'channels/{slug}/image.{extension}'.format(
        slug=channel.slug,
        extension=extension,
    )


def _channel_video_upload_to(channel, filename):
    extension = filename.split('.')[-1]
    return 'channels/{slug}/video.{extension}'.format(
        slug=channel.slug,
        extension=extension,
    )


class Channel(models.Model):

    objects = ChannelManager()

    tags = models.ManyToManyField(
        'Tag',
    )

    name = models.CharField(
        max_length=32,
        verbose_name='이름',
    )
    slug = models.SlugField(
    )

    image = models.ImageField(
        upload_to=_channel_image_upload_to,
        verbose_name='프로필 이미지',
    )
    video = models.FileField(
        upload_to=_channel_video_upload_to,
        verbose_name='대표 동영상',
    )

    description = models.TextField(
        verbose_name='설명',
    )

    is_display = models.BooleanField(
        blank=True,
        default=True,
        verbose_name='표시',
    )
    is_hot = models.BooleanField(
        blank=True,
        default=False,
        verbose_name='인기',
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
        verbose_name = '채널'
        verbose_name_plural = '채널'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('channels:detail', args=[self.slug])
