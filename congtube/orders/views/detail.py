from django.views.generic.detail import DetailView

from orders.models import Order

from iamport import Iamport


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        iamport = Iamport(
            imp_key='8161721766694252',
            imp_secret='kJqNZpHNzkWkA55fMJ9h1GyOm5ataB1vkrikRZ8qk4KUaQaWAjeB0MpmRAQ2bRxwjPRaP0B94m4fdecO'
        )

        pay_information = iamport.find(
            merchant_uid=self.object.merchant_uid
        )
        context['pay_info'] = pay_information
        return context

