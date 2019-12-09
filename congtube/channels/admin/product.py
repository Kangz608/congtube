from django.contrib import admin

from channels.models.product import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'channel',

        'name',
        'price',

        'is_display',
    )

    list_filter = (
        'is_display',

        'created_at',
    )

    search_fields = (
        'channel__name',

        'name',
    )


class ProductInline(admin.TabularInline):
    model = Product
