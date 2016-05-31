from edc_map.apps import EdcMapAppConfig


class BcppMapAppConfig(EdcMapAppConfig):
    name = 'bcpp_map'
    verbose_name = 'BCPP Mapper'
    mapper_model = ('bcpp_household', 'plot')
    mapper_survey_model = ('bcpp_survey', 'survey')

    def ready(self):
        from edc_map.site_mappers import site_mappers
        site_mappers.autodiscover()
