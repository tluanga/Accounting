from django.apps import AppConfig


class CashbookConfig(AppConfig):
    name = 'acm.cashbook'

    def ready(self):
        import acm.cashbook.signals
