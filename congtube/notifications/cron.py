from django.utils import timezone
from django.db.models import Q
from channels.models import Celebrity, Channel
from orders.models import Order
from notifications.views.kakao import Notification


def order_confirmations():
    n = Notification()
    day = int(timezone.now().strftime('%d'))
    today_orders = Order.objects.filter(
        Q(created_at__day=day) & Q(status=2)).values('channel__name','channel__slug').order_by('channel').distinct()
    for today_order in today_orders:
        name, slug = today_order['channel__name'], today_order['channel__slug']
        celebrity = Celebrity.objects.get(channel__name=name)
        celebrity_phonenumber = celebrity.phonenumber
        n.order_confirmations_alarm(celebrity_phonenumber, slug)
