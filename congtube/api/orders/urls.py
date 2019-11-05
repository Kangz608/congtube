from django.urls import path
from api.orders.views import OrderView


urlpatterns = [
    path('', OrderView.as_view()),
]
