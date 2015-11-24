# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20151123_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('active', models.BooleanField(default=True)),
                ('inventory', models.IntegerField(null=True, blank=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.RemoveField(
            model_name='variation',
            name='product',
        ),
        migrations.DeleteModel(
            name='Variation',
        ),
    ]
