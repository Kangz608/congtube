from django.views.generic.detail import DetailView

from channels.models.channel import Channel
from channels.models.product import Product


class ChannelOrderView(DetailView):
    model = Channel
    template_name = 'channels/order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(
            pk=self.request.GET.get('product_id')
        )
        return context
