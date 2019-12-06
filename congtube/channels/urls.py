from django.contrib.auth.decorators import login_required
from django.urls import path

from channels.views import *


app_name = 'channels'

urlpatterns = [
    path('', ChannelListView.as_view(), name='list'),
    path('<slug:slug>/', ChannelDetailView.as_view(), name='detail'),
    path('<slug:slug>/zBxD11Dj723jkmmj/', StarDetailView.as_view(), name='star'), # /star 추후 어려운 값으로 변경예정
    path('<slug:slug>/order/',
         login_required(ChannelOrderView.as_view()), name='order'),
]
