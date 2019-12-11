from django.utils import timezone
from django.db.models import Q
from channels.models import Celebrity, Channel
from orders.models import Order
from notifications.views.kakao import Notification


def order_confirmations():
    print('order_confirmations 실행')
    n = Notification()
    day = int(timezone.now().strftime('%d')) # 오늘 일수를 int형으로 앞에 0이 붙지 않게
    today_orders = Order.objects.filter(
        Q(created_at__day=day) & Q(status=2)).values('channel').order_by('channel').distinct()
        # 오늘 주문 온 사람들 중에서 결제완료인 채널명을 출력하라(중복제거)
    for today_order in today_orders:
        idx = today_order['channel'] # 제공자의 ID를 idx에 넣는다.
        ch = Channel.objects.get(pk=idx) # 제공자의 ID로 제공자(Channel) 테이블에서 정보를 꺼낸다.
        slug = ch.slug
        celebrity = Celebrity.objects.get(channel=ch) # 제공자 <-> 제공자개인정보
        celebrity_phonenumber = celebrity.phonenumber # 제공자개인정보에서 알림을 보내기 위한 폰 번호
        print('order_confirmations_alarm함수 실행 전')
        n.order_confirmations_alarm(celebrity_phonenumber, slug) # celebrity_phonenumber 를 인자값으로 넘겨준다.
        print('order_confirmations_alarm함수 실행 후')
