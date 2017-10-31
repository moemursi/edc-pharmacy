from django.contrib import admin
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import edc_pharma_admin
from ..forms import MedicationForm
from ..models import Medication
from .model_admin_mixin import ModelAdminMixin


@admin.register(Medication, site=edc_pharma_admin)
class MedicationAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MedicationForm

    fieldsets = (
        (None, {
            'fields': (
                'name',
                'measure',
                'units',
                'formulation',
                'route',
                'notes',
            )}), audit_fieldset_tuple
    )

    radio_fields = {
        'units': admin.VERTICAL,
        'formulation': admin.VERTICAL,
        'route': admin.VERTICAL
    }

    search_fields = ['name']
    ordering = ['name']
