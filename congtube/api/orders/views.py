from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from channels.models import Product
from orders.models import Order


class OrderView(APIView):
    def post(self, request, format=None):
        product = Product.objects.get(
            pk=request.data.get('product_pk')
        )

        order = Order.objects.create(
            user=request.user,
            product=product,

            status=Order.UNPAID,
            merchant_uid=request.data['merchant_uid'],
            reciever_name=request.data['reciever_name'],
            phonenumber=request.data['phonenumber'],
            email=request.data['email'],
            message=request.data['message'],
            amount=request.data['amount'],
        )

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                'detail': 'success',
                'order_id': order.id,
            }
        )
