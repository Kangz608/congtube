from django.contrib import admin

from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'user',
        'order',
        'product',
        'channel',

        'rating',
        'message',

        'is_display',
        'is_fake',

        'created_at',
    )

    list_filter = (
        'is_display',
        'is_fake',

        'rating',

        'created_at',
    )
