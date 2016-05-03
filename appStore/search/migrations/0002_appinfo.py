# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_name', models.CharField(max_length=100)),
                ('app_id', models.CharField(max_length=100)),
                ('developer', models.CharField(max_length=100)),
                ('developer_mailid', models.EmailField(max_length=75)),
                ('icon_url', models.URLField()),
                ('searchquery', models.ForeignKey(to='search.SearchQuery')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
