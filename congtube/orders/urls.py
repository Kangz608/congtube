from django.contrib.auth.decorators import login_required
from django.urls import path

from orders.views import *


app_name = 'orders'

urlpatterns = [
    path('<int:pk>/', OrderDetailView.as_view(), name='detail'),
    path('complete/', OrderCompleteView.as_view(), name='complete'),
]
