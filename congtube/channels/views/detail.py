from django.views.generic.detail import DetailView

from channels.models import Channel


class ChannelDetailView(DetailView):
    model = Channel
    template_name = 'channels/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channels'] = Channel.objects.exclude(pk=context['object'].id).order_by('?')[:4]

        return context
