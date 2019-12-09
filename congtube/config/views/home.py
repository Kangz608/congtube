from django.views.generic.base import TemplateView

from channels.models import Channel
from channels.models import Tag
from banners.models import Banner


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['channels'] = Channel.objects.is_display().random()
        context['tags'] = Tag.objects.all()
        context['banners'] = Banner.objects.is_display()

        return context
