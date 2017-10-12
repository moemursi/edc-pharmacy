from edc_base.model_mixins import ListModelMixin, BaseUuidModel

from django.db import models


class MedicationDefinition(ListModelMixin, BaseUuidModel):

    description = models.CharField(max_length=250,)

    total = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        blank=True,
        null=True)

    category = models.CharField(max_length=20,)

    storage_instructions = models.TextField(max_length=200)

    unit = models.CharField(max_length=20)

    milligram = models.CharField(max_length=200)

    number_of_times_per_day = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'edc_pharma'
