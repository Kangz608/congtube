from django.conf import settings

from storages.backends.s3boto3 import S3Boto3Storage

from django.contrib.staticfiles.storage import CachedFilesMixin, ManifestFilesMixin
from pipeline.storage import PipelineMixin


class S3PipelineManifestStorage(PipelineMixin, ManifestFilesMixin, S3Boto3Storage):
    pass


class S3PipelineCachedStorage(PipelineMixin, CachedFilesMixin, S3Boto3Storage):
    pass


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
        super(MediaStorage, self).__init__(*args, **kwargs)


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
        super(StaticStorage, self).__init__(*args, **kwargs)
