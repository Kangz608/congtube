from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'status',

        'user',
        'channel',
        'product',
        'amount',
        'video',

        'created_at',
    )

    list_filter = (
        'status',
        'created_at',
    )
