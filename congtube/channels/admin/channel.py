from django.contrib import admin

from channels.models import Channel, BestVideo

from .product import ProductInline
from .bestvideo import BestVideoInline


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'name',

        'is_display',
        'is_hot',
    )

    list_filter = (
        'is_display',
        'is_hot',

        'tags',
    )

    search_fields = (
        'name',
        'description',
    )

    inlines = (
        ProductInline,
        BestVideoInline,
    )


class ChannelInline(admin.TabularInline):
    model = Channel.tags.through