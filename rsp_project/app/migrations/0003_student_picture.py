# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_studentregister_form_filled'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'scanned_copy'),
        ),
    ]
