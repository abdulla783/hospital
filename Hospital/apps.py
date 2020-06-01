from django.apps import AppConfig


class HospitalConfig(AppConfig):
    name = 'Hospital'

    def ready(self):
        import Hospital.signals
