from django.urls import path
from api.reviews.views import ReviewView


urlpatterns = [
    path('', ReviewView.as_view()),
]
