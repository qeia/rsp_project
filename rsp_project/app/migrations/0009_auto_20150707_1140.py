# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='mobile_number_office',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='mobile_number_personal',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='mobile_number_residence',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='pi_number',
        ),
    ]
