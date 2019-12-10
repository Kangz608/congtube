from django.contrib import admin
from orders.models import Cancel


@admin.register(Cancel)
class CancelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display