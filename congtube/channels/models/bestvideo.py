from django.db import models


class ChannelQuerySet(models.QuerySet):

    def is_display(self):
        return self.filter(is_display=True)


class ChannelManager(models.Manager):

    def get_queryset(self):
        return ChannelQuerySet(self.model, using=self._db)

    def is_display(self):
        return self.get_queryset().is_display()


def _channel_video_upload_to(instance, filename):
    extension = filename.split('.')[-1]
    return 'channels/{slug}/best_video.{extension}'.format(
        slug=instance.channel.slug,
        extension=extension,
    )


class BestVideo(models.Model):

    objects = ChannelManager()

    channel = models.ForeignKey(
        'Channel',
        on_delete=models.CASCADE,
    )

    video = models.FileField(
        upload_to=_channel_video_upload_to,
        verbose_name='동영상',
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
        verbose_name = '베스트 비디오'
        verbose_name_plural = '베스트 비디오'

    def __str__(self):
        return str(self.channel) + '님의 베스트 비디오'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('channels:detail', args=[self.slug])
