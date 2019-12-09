from django.views.generic.base import TemplateView

from channels.models.channel import Channel
from channels.models.tag import Tag
from banners.models.banner import Banner


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['channels'] = Channel.objects.is_display().random()
        context['tags'] = Tag.objects.all()
        context['banners'] = Banner.objects.is_display()

        return context
