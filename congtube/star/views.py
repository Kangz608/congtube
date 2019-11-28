from orders.models.order import Order
from django.views.generic.detail import DetailView


class StarDetailView(DetailView):
    model = Order
    template_name = 'star/test.html'
    slug_field = 'amount'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(pk=context['object'].id)

        return context