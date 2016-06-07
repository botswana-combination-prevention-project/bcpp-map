from datetime import datetime, time

from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from edc_map.mapper import Mapper
from edc_device.device import Device
from bcpp_map.choices import SECTIONS, SUB_SECTIONS


class BasePlotMapper(Mapper):

    app_config = django_apps.get_app_config('bcpp_map')
    clinic_days = {}
    intervention = None
    location_boundary = None
    map_code = None
    pair = None
    survey_dates = {}
    regions = SECTIONS
    sections = SUB_SECTIONS

    def __init__(self):
        super(BasePlotMapper, self).__init__()
        self.active = None
        if settings.CURRENT_COMMUNITY == self.map_area:
            self.active = True
        if self.intervention is None:
            self.intervention_code = None
        else:
            self.intervention_code = 'CPC' if self.intervention else 'ECC'

    def __repr__(self):
        return '{}(\'{}\')'.format(self.__class__.__name__, self.map_area)

    def __str__(self):
        return '{}{} ({}){}'.format(self.map_area[0].upper(), self.map_area[1:], self.intervention_code,
                                    ' *active' if self.active else '')

    @property
    def __dict__(self):
        dct = super(BasePlotMapper, self).__dict__
        return dct.update({
            'map_code': self.map_code,
            'intervention': self.intervention,
            'survey_dates': self.survey_dates,
            'clinic_days': self.clinic_days})

    def verify_survey_dates(self):
        """Verifies that the dates fall within the survey for the current community."""
        Survey = self.survey_model
        for survey_slug, survey_dates in self.survey_dates.iteritems():
            try:
                if self.active and survey_slug == settings.CURRENT_SURVEY:
                    start_datetime = datetime.combine(survey_dates.start_date, time.min)
                    Survey.objects.current_survey(
                        report_datetime=start_datetime,
                        survey_slug=survey_slug,
                        datetime_label='start_datetime',
                        community=self.map_area)
                    full_enrollment_datetime = datetime.combine(
                        survey_dates.full_enrollment_date, time.min)
                    Survey.objects.current_survey(
                        report_datetime=full_enrollment_datetime,
                        survey_slug=survey_slug,
                        datetime_label='full_enrollment_date',
                        community=self.map_area)
                    end_datetime = datetime.combine(survey_dates.end_date, time.min)
                    Survey.objects.current_survey(
                        report_datetime=end_datetime,
                        survey_slug=survey_slug,
                        datetime_label='end_datetime',
                        community=self.map_area)
            except Survey.DoesNotExist:
                raise ImproperlyConfigured('Date does not fall within defined Survey instance. '
                                           'See mapper and Survey for {}.'.format(survey_slug))
            except ImproperlyConfigured as err_message:
                raise ImproperlyConfigured('{}:{} survey {}. {}'.format(self.map_code, self.map_area,
                                                                        settings.CURRENT_SURVEY,
                                                                        err_message))

    @property
    def test_location(self):
        """Decimal Degrees = Degrees + minutes/60 + seconds/3600"""
        degrees_e, minutes_e = self.deg_to_dms(self.center_lon)
        degrees_s, minutes_s = self.deg_to_dms(self.center_lat)
        return (degrees_s, minutes_s, degrees_e, minutes_e)

    @property
    def current_survey_slug(self):
        """Returns the survey_slug from the Survey instance using settings.CURRENT_SURVEY."""
        return self.survey_model.objects.current_survey(survey_slug=settings.CURRENT_SURVEY).survey_slug

    @property
    def current_survey_dates(self):
        return self.survey_dates.get(self.current_survey_slug)

    @property
    def current_clinic_days(self):
        return self.clinic_days.get(self.current_survey_slug)

    @property
    def clinic_plot(self):
        """Returns and, if needed, creates a non-residential plot to represent the CLINIC."""
        # We can only do this on community servers, not on netbooks or central server.
        device = Device()
        Plot = self.item_model
        try:
            plot = Plot.objects.get(plot_identifier=self.clinic_plot_identifier)
        except Plot.DoesNotExist:
            if device.is_community_server:
                plot = Plot.objects.create(
                    plot_identifier=self.clinic_plot_identifier,
                    household_count=1,
                    status='bcpp_clinic',
                    community=self.map_area,
                    action='confirmed',
                    description=('{} clinic').format(self.map_area))
            else:
                plot = Plot(
                    plot_identifier=self.clinic_plot_identifier,
                    household_count=1,
                    status='bcpp_clinic',
                    community=self.map_area,
                    action='confirmed',
                    description=('{} clinic').format(self.map_area))
        return plot

    @property
    def clinic_plot_identifier(self):
        if not self.map_code:
            raise TypeError('Expected a value for mapper.map_code, Got None.')
        return '{}0000-00'.format(self.map_code)

    @property
    def community(self):
        return self.map_area
