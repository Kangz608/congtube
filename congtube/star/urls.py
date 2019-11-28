from django.urls import path
from star.views import *


app_name = 'star'

urlpatterns = [
    path('<slug:slug>/', StarDetailView.as_view(), name='detail'),
]
