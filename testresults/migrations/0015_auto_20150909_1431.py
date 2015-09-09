# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testresults', '0014_auto_20150909_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='worst_limit',
            field=models.CharField(db_index=True, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='worst_limit_nontest',
            field=models.CharField(db_index=True, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='worst_limit_nontest_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='worst_limit_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='worst_limit_test',
            field=models.CharField(db_index=True, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='worst_limit_test_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
