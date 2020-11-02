from django.apps import AppConfig


class TrialConfig(AppConfig):
    name = 'acm.trial'

    def ready(self):
        import acm.trial.signals
