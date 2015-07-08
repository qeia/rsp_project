# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150706_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregister',
            name='employee',
            field=models.ForeignKey(related_name='em', primary_key=True, serialize=False, to='app.Employee'),
        ),
    ]
