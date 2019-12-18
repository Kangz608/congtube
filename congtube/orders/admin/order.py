from django.contrib import admin
from orders.models import Order
from iamport import Iamport
from notifications.views import Notification


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'status',

        'user',
        'channel',
        'product',
        'amount',
        'video',
        'is_alarm',
        'cancel',
        'created_at',
    )

    list_filter = (
        'status',
        'created_at',
    )

    def save_model(self, request, obj, form, change):
        if change: # 변경이 감지되면
            n = Notification()
            if obj.status == 3 and obj.video and obj.is_alarm: # 주문완료(3) and 영상업로드 알림 전송(v) and
                n.video_complete(obj.phonenumber, obj.user, obj.channel) # 비디오 완성 알림
                obj.save()
                # 주문취소 발생 시
            elif obj.status == 4 and obj.cancelreason and obj.cancel:
                iamport = Iamport(
                    imp_key='8161721766694252',
                    imp_secret='kJqNZpHNzkWkA55fMJ9h1GyOm5ataB1vkrikRZ8qk4KUaQaWAjeB0MpmRAQ2bRxwjPRaP0B94m4fdecO'
                ) # 알림이 발생이 안하면 이미 주문이 취소 된 건이다.
                try:
                    # 상품 아이디로 취소
                    iamport.cancel(u'취소하는 이유', merchant_uid=obj.merchant_uid)
                except Iamport.ResponseError as e:
                    print
                    e.code
                    print
                    e.message  # 에러난 이유를 알 수 있음
                except Iamport.HttpError as http_error:
                    print
                    http_error.code
                    print
                    http_error.reason  # HTTP not 200 에러난 이유를 알 수 있음
                else: # 에러가 발생하지 않았다면 아래 구문 실행
                    # [!] 주문취소 알람발생
                    n.payment_cancel(obj.phonenumber, obj.user, obj.channel, obj.created_at, obj.cancelreason)
                    obj.save()
