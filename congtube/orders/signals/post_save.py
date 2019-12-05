from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models.order import Order
from notifications.views.kakao import Notification
from channels.models import Celebrity


@receiver(post_save, sender=Order)  # Sender=Order, Order 테이블에서 post_save 발생 시
def post_save_order(instance, created, **kwargs):  # order() 가 입력되면 실행
    n = Notification()
    if instance.status == 2: # 주문완료 시 카카오 알림 발생
        n.payment_complete(instance.phonenumber, instance.user, instance.product.name, instance.amount)

