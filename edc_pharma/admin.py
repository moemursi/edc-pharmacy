from django.contrib import admin
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse

from simple_history.admin import SimpleHistoryAdmin
from edc_base.modeladmin.mixins import (
    ModelAdminBasicMixin, ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminFormInstructionsMixin)

from edc_pharma.admin_site import edc_pharma_admin
from edc_pharma.forms.dispense_form import DispenseForm
from edc_pharma.models.dispense import Dispense
from edc_pharma.models.medication import Medication
from edc_pharma.models.patient import Patient
from edc_pharma.models.protocol import Protocol
from edc_pharma.models.site import Site


class BaseModelAdmin(ModelAdminBasicMixin, ModelAdminFormAutoNumberMixin, ModelAdminFormInstructionsMixin,
                     ModelAdminAuditFieldsMixin):
    pass


@admin.register(Dispense, site=edc_pharma_admin)
class DispenseAdmin(BaseModelAdmin, admin.ModelAdmin):
    form = DispenseForm
    list_display = ('patient', 'medication', 'prepared_datetime',)
    list_filter = ('prepared_datetime', 'medication',)
    inlines = []

    radio_fields = {'dispense_type': admin.VERTICAL}

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect(
            reverse('home_url', kwargs={'subject_identifier': str(obj.patient.subject_identifier)}))

    def response_change(self, request, obj):
        return HttpResponseRedirect(
            reverse('home_url', kwargs={'subject_identifier': str(obj.patient.subject_identifier)}))


@admin.register(Patient, site=edc_pharma_admin)
class PatientAdmin(BaseModelAdmin, admin.ModelAdmin):
    list_display = ('initials', 'consent_date',)
    list_filter = ('consent_date',)
    inlines = []

    radio_fields = {'gender': admin.VERTICAL}

    def response_add(self, request, obj, post_url_continue=None):
        return HttpResponseRedirect(
            reverse('home_url', kwargs={'subject_identifier': str(obj.subject_identifier)}))


@admin.register(Medication, site=edc_pharma_admin)
class MedicationAdmin(BaseModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'storage_instructions',)
    list_filter = ('name', )
    inlines = []


@admin.register(Site, site=edc_pharma_admin)
class SiteAdmin(BaseModelAdmin, admin.ModelAdmin):
    list_display = ('protocol', 'site_code', 'telephone_number',)
    list_filter = ('site_code',)
    inlines = []


@admin.register(Protocol, site=edc_pharma_admin)
class ProtocolAdmin(BaseModelAdmin, admin.ModelAdmin):
    list_display = ('number', 'name',)
    list_filter = ('number',)
    inlines = []


admin.site.register(Patient, SimpleHistoryAdmin)
admin.site.register(Medication, SimpleHistoryAdmin)
