# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_student_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'media'),
        ),
        migrations.AlterField(
            model_name='studentregister',
            name='employee',
            field=models.ForeignKey(related_name='employee', primary_key=True, serialize=False, to='app.Employee'),
        ),
    ]
