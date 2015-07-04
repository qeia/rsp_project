# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=230, serialize=False, primary_key=True)),
                ('mobile_number', models.BigIntegerField()),
                ('first_name_r', models.CharField(max_length=30)),
                ('last_name_r', models.CharField(max_length=30)),
                ('email_id_r', models.EmailField(max_length=230)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRegister',
            fields=[
                ('employee', models.ForeignKey(primary_key=True, serialize=False, to='app.Employee')),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('key_expires', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_register', models.ForeignKey(primary_key=True, serialize=False, to='app.StudentRegister')),
                ('college_name', models.CharField(default=b'nit', max_length=250)),
                ('department_choice', models.IntegerField(default=0)),
            ],
        ),
    ]
