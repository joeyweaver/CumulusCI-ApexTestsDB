# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testresults', '0003_auto_20150205_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='duration',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
