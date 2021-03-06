from dateutil.relativedelta import MO, TU, WE, TH, FR
from datetime import date

from edc_map.site_mappers import site_mappers


from ..choices import SECTIONS, SUB_SECTIONS
from ..constants import BASELINE_SURVEY_SLUG
from ..landmarks import BOKAA_LANDMARKS
from ..structures import ClinicDaysTuple, SurveyDatesTuple

from .base_plot_mapper import BasePlotMapper


class BokaaPlotMapper(BasePlotMapper):

    center_lat = -24.425856
    center_lon = 26.021626
    intervention = False
    landmarks = BOKAA_LANDMARKS
    location_boundary = ()
    map_area = 'bokaa'
    map_code = '17'
    pair = 4
    radius = 5.5
    regions = SECTIONS
    sections = SUB_SECTIONS

    survey_dates = {
        BASELINE_SURVEY_SLUG: SurveyDatesTuple(
            name='bhs',
            start_date=date(2014, 11, 5),
            full_enrollment_date=date(2014, 11, 28),
            end_date=date(2014, 12, 20),
            smc_start_date=date(2014, 12, 5)),
        'bcpp-year-2': SurveyDatesTuple(
            name='t1',
            start_date=date(2015, 11, 9),
            full_enrollment_date=date(2015, 11, 29),
            end_date=date(2015, 11, 29),
            smc_start_date=date(2015, 12, 5)),
        'bcpp-year-3': SurveyDatesTuple(
            name='t2',
            start_date=None,
            full_enrollment_date=None,
            end_date=None,
            smc_start_date=None),
    }

    clinic_days = {
        BASELINE_SURVEY_SLUG: {
            'IDCC': ClinicDaysTuple((WE, ), None),
            'ANC': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'VCT': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'SMC': ClinicDaysTuple((FR, ), survey_dates[BASELINE_SURVEY_SLUG].smc_start_date)},
        'bcpp-year-2': {
            'IDCC': ClinicDaysTuple((WE, ), None),
            'ANC': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'VCT': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'SMC': ClinicDaysTuple((FR, ), survey_dates['bcpp-year-2'].smc_start_date)},
    }

site_mappers.register(BokaaPlotMapper)
