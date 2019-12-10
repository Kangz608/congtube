from django.contrib import admin

from channels.models import BestVideo



@admin.register(BestVideo)
class BestVideoAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'video',
        'is_display'
    )

    list_filter = (
        'is_display',

        'created_at',
    )

class BestVideoInline(admin.TabularInline):
    model = BestVideo
    extra = 1