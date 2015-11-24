# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20151116_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonateItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('quentity', models.IntegerField()),
                ('zipcode', models.CharField(max_length=6)),
                ('discription', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(null=True, blank=True)),
                ('expiry_date', models.DateTimeField(null=True, blank=True)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(to='products.DonateItems'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='product',
            field=models.ForeignKey(to='products.DonateItems'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
