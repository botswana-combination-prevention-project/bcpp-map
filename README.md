# bcpp-map
Mapper classes for BCPP

## Installation

    pip install bcpp_map

Include in settings.INSTALLED_APPS:

    INSTALLED_APPS = [
    ...
    'bcpp_map',
    ...
    ]

## To use with models other than the defaults:

Declare an `AppConfig`;

    class MyMapAppConfig(EdcMapAppConfig):
        name = 'bcpp_map'
        verbose_name = 'My BCPP Mappers'
        mapper_model = ('my_app', 'my_model')
        mapper_survey_model = ('my_app', 'my_survey_model')
        
Include in settings.INSTALLED_APPS:

    INSTALLED_APPS = [
    ...
    'my_map.apps.MyMapAppConfig',
    ...
    ]
    
### Issues

If survey model does not exist with print a warning when the AppConfig.ready from `edc_map` loads the sites_mappers
      

