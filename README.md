# bcpp-map
Mapper classes for BCPP

## Installation

    pip install git+https://github.com/botswana-harvard/bcpp-map@develop#egg=bcpp_map

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
    
### Other examples

See `bcpp_interview`

### Issues

The mappers have a fair amount of BCPP specific code. Maybe the `mappers` try to do too much. However, other studies can still use the mappers to help locate subjects.  

### Warning on load

If survey model does not exist `edc_map.AppConfig.ready` prints a warning based on the `LookupError` from `get_model`.
      

