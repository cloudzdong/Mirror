# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Days6_Weather',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Temp', models.CharField(max_length=50)),
                ('Wea', models.CharField(max_length=60)),
                ('Wind', models.CharField(max_length=60)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DayTime_Weather',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Top_Temp', models.CharField(max_length=20)),
                ('DTWea', models.CharField(max_length=50)),
                ('DTWind', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Feels_Like', models.CharField(max_length=20)),
                ('Current_Temp', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NightTime_Weather',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Low_Temp', models.CharField(max_length=20)),
                ('NTWea', models.CharField(max_length=50)),
                ('NTWind', models.CharField(max_length=60)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
