from django.urls import path, include


app_name = 'api'

urlpatterns = [
    path('orders/', include('api.orders.urls')),
    path('reviews/', include('api.reviews.urls')),
]
