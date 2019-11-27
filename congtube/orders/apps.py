from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'

    def ready(self):
        from orders.signals.pre_save import pre_save_order
        from orders.signals.post_save import post_save_order

