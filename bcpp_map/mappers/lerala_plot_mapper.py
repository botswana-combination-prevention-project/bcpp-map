from dateutil.relativedelta import MO, TU, WE, TH, FR
from datetime import date

from edc_map.site_mappers import site_mappers

from ..choices import SECTIONS, SUB_SECTIONS
from ..constants import BASELINE_SURVEY_SLUG
from ..landmarks import LERALA_LANDMARKS
from ..structures import ClinicDaysTuple, SurveyDatesTuple

from .base_plot_mapper import BasePlotMapper


class LeralaPlotMapper(BasePlotMapper):

    map_area = 'lerala'
    map_code = '21'
    pair = 6
    regions = SECTIONS
    sections = SUB_SECTIONS

    landmarks = LERALA_LANDMARKS

    intervention = True

    center_lat = -22.7830257
    center_lon = 27.7605844
    radius = 5.5
    location_boundary = ()

    survey_dates = {
        BASELINE_SURVEY_SLUG: SurveyDatesTuple(
            name='bhs',
            start_date=date(2015, 1, 19),
            full_enrollment_date=date(2015, 2, 10),
            end_date=date(2015, 3, 3),
            smc_start_date=date(2015, 2, 13)),
        'bcpp-year-2': SurveyDatesTuple(
            name='t1',
            start_date=date(2016, 2, 12),
            full_enrollment_date=date(2016, 3, 20),
            end_date=date(2016, 3, 21),
            smc_start_date=date(2016, 2, 12)),
        'bcpp-year-3': SurveyDatesTuple(
            name='t2',
            start_date=date(2016, 12, 4),
            full_enrollment_date=date(2016, 12, 31),
            end_date=date(2016, 12, 31),
            smc_start_date=date(2016, 12, 31)),
    }

    clinic_days = {
        BASELINE_SURVEY_SLUG: {
            'IDCC': ClinicDaysTuple((MO, WE), None),
            'ANC': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'VCT': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'SMC': ClinicDaysTuple((MO, TU, WE, TH, FR), survey_dates[BASELINE_SURVEY_SLUG].smc_start_date)},
        'bcpp-year-2': {
            'IDCC': ClinicDaysTuple((MO, ), None),
            'ANC': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'VCT': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'SMC': ClinicDaysTuple((MO, TU, WE, TH, FR), survey_dates['bcpp-year-2'].smc_start_date)},
    }

site_mappers.register(LeralaPlotMapper)
