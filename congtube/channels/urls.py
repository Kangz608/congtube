from django.contrib.auth.decorators import login_required
from django.urls import path

from channels.views import *


app_name = 'channels'

urlpatterns = [
    path('', ChannelListView.as_view(), name='list'),
    path('<slug:slug>/', ChannelDetailView.as_view(), name='detail'),
    path('<slug:slug>/order/',
         login_required(ChannelOrderView.as_view()), name='order'),
]
