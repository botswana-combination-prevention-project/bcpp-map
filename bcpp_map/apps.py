from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'bcpp_map'
    verbose_name = 'BCPP Mapper'
