from django.contrib.sitemaps import Sitemap

from channels.models import Channel


class ChannelSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Channel.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
