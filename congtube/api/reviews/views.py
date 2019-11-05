from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from orders.models import Order
from reviews.models import Review


class ReviewView(APIView):
    def post(self, request, format=None):

        order = Order.objects.get(
            pk=request.data.get('order_id')
        )

        review = Review.objects.create(
            user=request.user,
            order=order,
            rating=request.data.get('rating'),
            message=request.data.get('message'),
        )

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                'detail': 'success',
                'review_id': review.id,
            }
        )
