# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20151123_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='price',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='saleprice',
        ),
    ]
