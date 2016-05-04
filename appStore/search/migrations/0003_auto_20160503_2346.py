# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_appinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appinfo',
            old_name='app_id',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='appinfo',
            old_name='app_name',
            new_name='url',
        ),
    ]
