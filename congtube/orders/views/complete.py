from django.views.generic.base import TemplateView

from orders.models import Order
from channels.models import Channel

from iamport import Iamport


class OrderCompleteView(TemplateView):
    template_name = 'orders/complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['channels'] = Channel.objects.order_by('?')[:4]

        try:
            order = Order.objects.get(
                merchant_uid=self.request.GET['merchant_uid']
            )

            iamport = Iamport(
                imp_key='8161721766694252',
                imp_secret='kJqNZpHNzkWkA55fMJ9h1GyOm5ataB1vkrikRZ8qk4KUaQaWAjeB0MpmRAQ2bRxwjPRaP0B94m4fdecO'
            )
            is_paid = iamport.is_paid(
                order.product.price,
                merchant_uid=self.request.GET['merchant_uid']
            )

            if is_paid is True:
                order.status = Order.PAID
                order.save()

            context['order'] = order
        except Exception as e:
            order = {
                'status': Order.UNPAID,
            }
            context['order'] = order
        return context
