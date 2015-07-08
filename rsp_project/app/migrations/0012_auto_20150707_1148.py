# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20150707_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='duration',
            field=models.IntegerField(default=15, choices=[(15, 15), (30, 30), (45, 45), (60, 60)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
