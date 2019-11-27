from django.contrib import admin
from ..models.cancel import Cancel

@admin.register(Cancel)
class CancelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display