# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-20 04:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctorinfo', '0002_auto_20181120_1003'),
        ('comment', '0001_initial'),
        ('patientinfo', '0002_medicine'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='comment.Comment'),
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='related_doc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='doctorinfo.DoctorProfile'),
        ),
    ]
