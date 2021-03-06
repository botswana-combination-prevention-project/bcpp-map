from dateutil.relativedelta import MO, TU, WE, TH, FR

from datetime import date

from edc_map.site_mappers import site_mappers

from ..choices import SECTIONS, SUB_SECTIONS
from ..constants import BASELINE_SURVEY_SLUG
from ..landmarks import DIGAWANA_LANDMARKS
from ..structures import ClinicDaysTuple, SurveyDatesTuple

from .base_plot_mapper import BasePlotMapper


class TestPlotMapper(BasePlotMapper):

    map_area = 'test_community'
    map_code = '01'
    pair = 0
    regions = SECTIONS
    sections = SUB_SECTIONS

    landmarks = DIGAWANA_LANDMARKS

    center_lat = -25.330451
    center_lon = 25.556502
    radius = 3.5
    location_boundary = ()

    intervention = True

    survey_dates = {
        BASELINE_SURVEY_SLUG: SurveyDatesTuple(
            name='bhs',
            start_date=date(2016, 3, 1),
            full_enrollment_date=date(2016, 4, 30),
            end_date=date(2016, 4, 30),
            smc_start_date=date(2016, 4, 30)),
        'bcpp-year-2': SurveyDatesTuple(
            name='t1',
            start_date=date(2016, 4, 11),
            full_enrollment_date=date(2016, 6, 30),
            end_date=date(2016, 6, 30),
            smc_start_date=date(2016, 6, 30)),
        'bcpp-year-3': SurveyDatesTuple(
            name='t2',
            start_date=date(2016, 10, 11),
            full_enrollment_date=date(2016, 12, 30),
            end_date=date(2016, 12, 30),
            smc_start_date=date(2016, 12, 30)),
    }

    clinic_days = {
        BASELINE_SURVEY_SLUG: {
            'IDCC': ClinicDaysTuple((MO, WE), None),
            'ANC': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'VCT': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'SMC': ClinicDaysTuple((MO, TU, WE, TH, FR), survey_dates[BASELINE_SURVEY_SLUG].smc_start_date)},
        'bcpp-year-2': {
            'IDCC': ClinicDaysTuple((MO, WE), None),
            'ANC': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'VCT': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'SMC': ClinicDaysTuple((MO, TU, WE, TH, FR), survey_dates['bcpp-year-2'].smc_start_date)},
        'bcpp-year-3': {
            'IDCC': ClinicDaysTuple((MO, WE), None),
            'ANC': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'VCT': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'SMC': ClinicDaysTuple((MO, TU, WE, TH, FR), survey_dates['bcpp-year-3'].smc_start_date)},
    }

site_mappers.register(TestPlotMapper)
