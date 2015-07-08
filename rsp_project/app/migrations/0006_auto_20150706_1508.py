# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150706_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregister',
            name='employee',
            field=models.ForeignKey(primary_key=True, serialize=False, to='app.Employee'),
        ),
    ]
