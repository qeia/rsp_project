# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20150707_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mobile_number_personal',
            field=models.BigIntegerField(),
        ),
    ]
