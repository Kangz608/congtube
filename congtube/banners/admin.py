from django.contrib import admin
from banners.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'title',
        'image',
        'url',
        'is_display',
        'created_at',
    )

    list_filter = (
        'created_at',
        'is_display',
    )
