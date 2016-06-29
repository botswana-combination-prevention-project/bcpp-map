from edc_map.apps import EdcMapAppConfig


class BcppMapAppConfig(EdcMapAppConfig):
    name = 'bcpp_map'
    verbose_name = 'BCPP Mapper'
    mapper_model = ('bcpp_household', 'plot')
    mapper_survey_model = ('bcpp_survey', 'survey')
