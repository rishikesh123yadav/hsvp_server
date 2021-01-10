from django.apps import AppConfig


class HsvpConfig(AppConfig):
    name = 'hsvp'

    def ready(self):
        import hsvp.signals
