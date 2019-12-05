from django.utils import timezone
from channels.models import Celebrity
from django.db.models import Q
from orders.models import Order
from channels.models import Channel


def order_confirmations():
    now = timezone.now().strftime('%d')
    order = Order.objects.filter(
        Q(created_at__day=now) & Q(status=2).values('channel').order_by('channel').distinct())
    print(order) # <QuerySet [{'channel': 1}, {'channel': 3}]>
    for orders in order:
        idx = orders['channel'] # {'channel': 1}, {'channel': 3} : 1, 3
        ch = Channel.objects.get(pk=idx)
        celebrity = Celebrity.objects.get(channel=ch)
        phonenumber = celebrity.phonenumber