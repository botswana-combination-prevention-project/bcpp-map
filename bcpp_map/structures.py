from collections import namedtuple

ClinicDaysTuple = namedtuple('ClinicDaysTuple', 'days start_date')
SurveyDatesTuple = namedtuple(
    'SurveyDatesTuple', 'name start_date full_enrollment_date end_date smc_start_date')
