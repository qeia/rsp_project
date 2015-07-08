# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20150707_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile_number_office',
            field=models.BigIntegerField(),
        ),
    ]
