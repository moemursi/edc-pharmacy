from dateutil.relativedelta import relativedelta
from django.apps import apps as django_apps
from django.db import models


class DispenseAppointmentMixin(models.Model):

    facility_name = models.CharField(
        max_length=25)

    visit_code_sequence = models.IntegerField(
        verbose_name=('Sequence'),
        default=0,
        null=True,
        blank=True,
        help_text=('An integer to represent the sequence of additional '
                   'appointments relative to the base appointment, 0, needed '
                   'to complete data collection for the timepoint. (NNNN.0)'))

    appt_datetime = models.DateTimeField(
        verbose_name=('Appointment date and time'),
        help_text='',
        db_index=True)

    dispense_datetime = models.DateTimeField(
        verbose_name=('Dispense date and time'),
        help_text='',
        null=True,
        blank=True)

    appt_reason = models.CharField(
        verbose_name=('Reason for appointment'),
        max_length=25,
        help_text=('Reason for appointment'),
        blank=True)

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50, null=True, blank=True)

    comment = models.CharField(
        'Comment',
        max_length=250,
        blank=True)

    def previous(self):
        return self.__class__.objects.filter(
            schedule=self.schedule, appt_datetime__lt=self.appt_datetime
        ).order_by('appt_datetime').first()

    def next(self):
        return self.__class__.objects.filter(
            schedule=self.schedule, appt_datetime__gt=self.appt_datetime
        ).order_by('appt_datetime').first()

    def completed(self):
        return self.__class__.objects.filter(
            schedule=self.schedule, is_dispensed=True
        ).order_by('appt_datetime')

    def next_timepoints(self):
        return self.__class__.objects.filter(
            schedule=self.schedule, appt_datetime__gt=self.appt_datetime,
            is_dispensed=False
        ).order_by('appt_datetime')

    @property
    def print_profile(self):
        from ..dispense_plan import dispense_plans
        control_arm = dispense_plans.get(self.schedule.arm)
        schedule_plan = control_arm.get(self.schedule.name)
        profiles = schedule_plan.get('dispense_profile')
        return profiles.get(self.profile_label.split('.')[0])

    @property
    def profile_medications(self):
        medications = []
        for _, value in self.print_profile.medication_types.items():
            medications.append(value)
        return medications

    @property
    def next_appt_datetime(self):
        next_appt = self.next()
        if next_appt:
            return (next_appt.appt_datetime - relativedelta(days=2))

    def update_next_dispense_datetime(self):
        """Update the next appointment dispense datetime."""
        app_config = django_apps.get_app_config('edc_pharma')
        next_appt = self.next()
        if self.next_appt_datetime:
            # FIX use facility to check for day availability.
            #             facility = app_config.facility
            next_appt.dispense_datetime = self.next_appt_datetime
            next_appt.save()
        return next_appt

    class Meta:
        abstract = True