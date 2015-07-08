# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_studentregister_form_filled'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='mobile_number',
            new_name='mobile_number_office',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name_r',
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.CharField(default='fl', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(default='fl', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='mobile_number_personal',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='mobile_number_residence',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='pi_number',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='relation',
            field=models.CharField(default='s', max_length=2, choices=[(b's', b'Son'), (b'd', b'Daughter'), (b'or', b'Other')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='branch',
            field=models.CharField(default='s', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='duration',
            field=models.IntegerField(default=15, choices=[(15, 15), (30, 30), (45, 45), (60, 60)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'media'),
        ),
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.CharField(default='m', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='department_choice',
            field=models.CharField(max_length=100),
        ),
    ]
