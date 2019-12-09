from django.contrib import admin

from channels.models.tag import Tag

from .channel import ChannelInline


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'name',
        'slug',
    )

    inlines = (
        ChannelInline,
    )
