from dateutil.relativedelta import MO, TU, WE, TH, FR
from datetime import date

from edc_map.site_mappers import site_mappers

from ..choices import SECTIONS, SUB_SECTIONS
from ..constants import BASELINE_SURVEY_SLUG
from ..landmarks import TATI_SIDING_LANDMARKS
from ..structures import ClinicDaysTuple, SurveyDatesTuple

from .base_plot_mapper import BasePlotMapper


class TatiSidingPlotMapper(BasePlotMapper):

    map_area = 'tati_siding'
    map_code = '30'
    pair = 9
    regions = SECTIONS
    sections = SUB_SECTIONS

    landmarks = TATI_SIDING_LANDMARKS

    intervention = True

    center_lat = -21.274018
    center_lon = 27.474822
    radius = 6.5
    location_boundary = ()

    survey_dates = {
        BASELINE_SURVEY_SLUG: SurveyDatesTuple(
            name='bhs',
            start_date=date(2015, 5, 1),
            full_enrollment_date=date(2015, 5, 31),
            end_date=date(2015, 6, 21),
            smc_start_date=date(2015, 8, 10)),
        'bcpp-year-2': SurveyDatesTuple(
            name='t1',
            start_date=date(2016, 5, 19),
            full_enrollment_date=date(2016, 6, 10),
            end_date=date(2016, 6, 10),
            smc_start_date=date(2016, 6, 10)),
        'bcpp-year-3': SurveyDatesTuple(
            name='t2',
            start_date=None,
            full_enrollment_date=None,
            end_date=None,
            smc_start_date=None),
    }

    clinic_days = {
        BASELINE_SURVEY_SLUG: {
            'IDCC': ClinicDaysTuple((MO, WE, ), None),
            'ANC': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'VCT': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'SMC': ClinicDaysTuple((MO, TU, WE, TH, FR), survey_dates[BASELINE_SURVEY_SLUG].smc_start_date)},
        'bcpp-year-2': {
            'IDCC': ClinicDaysTuple((MO, WE), None),
            'ANC': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'VCT': ClinicDaysTuple((MO, TU, WE, TH, FR), None),
            'SMC': ClinicDaysTuple((MO, TU, WE, TH, FR), survey_dates['bcpp-year-2'].smc_start_date)},
    }

site_mappers.register(TatiSidingPlotMapper)
