from django.utils import timezone
from channels.models import Celebrity
from django.db.models import Q
from orders.models import Order
from channels.models import Channel
from notifications.views.kakao import Notification


def order_confirmations():
    print('order_confirmations1')
    n = Notification
    day = int(timezone.now().strftime('%d'))
    today_order = Order.objects.filter(
        Q(created_at__day=day) & Q(status=2)).values('channel').order_by('channel').distinct()

    for torder in today_order:
        print('order_confirmations2')
        idx = torder['channel'] # 제공자의 ID를 idx에 넣는다.
        ch = Channel.objects.get(pk=idx) # 제공자의 ID로 제공자(Channel) 테이블에서 정보를 꺼낸다.
        celebrity = Celebrity.objects.get(channel=ch) # 제공자 <-> 제공자개인정보
        celebrity_phonenumber = celebrity.phonenumber # 제공자개인정보에서 알림을 보내기 위한 폰 번호
        n.order_confirmations_alarm() # 를 인자값으로 넘겨준다.