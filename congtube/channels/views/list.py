from django.views.generic.list import ListView

from channels.models.channel import Channel
from channels.models.tag import Tag
from banners.models import Banner


class ChannelListView(ListView):
    model = Channel
    template_name = 'channels/list.html'
    context_object_name = 'channels'

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search')
        queryset = super().get_queryset(**kwargs)

        if search:
            return queryset.filter(name__contains=search)

        return queryset.is_display().random()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['banners'] = Banner.objects.filter(is_display=True)

        search = self.request.GET.get('search')
        if search:
            context['search'] = search

        return context
