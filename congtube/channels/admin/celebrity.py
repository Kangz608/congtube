from django.contrib import admin
from channels.models import Celebrity


@admin.register(Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'channel',
        'phonenumber',
    )

