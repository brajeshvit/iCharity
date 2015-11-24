# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20151123_1036'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DonateItems',
            new_name='Product',
        ),
    ]
