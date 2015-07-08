# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20150707_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='first_name_r',
            new_name='name_r',
        ),
        migrations.AddField(
            model_name='student',
            name='sem',
            field=models.IntegerField(default=4, choices=[(4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=25),
        ),
    ]
