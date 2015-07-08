# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20150707_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile_number_residence',
            field=models.BigIntegerField(),
        ),
    ]
