# Generated by Django 2.0rc1 on 2017-11-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_pharmacy', '0002_auto_20171120_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='facility_name',
            field=models.CharField(help_text='set by model that creates appointments, e.g. Enrollment', max_length=25),
        ),
    ]