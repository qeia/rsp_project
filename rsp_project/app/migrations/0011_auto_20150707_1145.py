# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_employee_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(default=b'oakf', max_length=40),
        ),
        migrations.AddField(
            model_name='employee',
            name='mobile_number_office',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='employee',
            name='mobile_number_personal',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='employee',
            name='mobile_number_residence',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='employee',
            name='pi_number',
            field=models.BigIntegerField(default=1),
        ),
    ]
