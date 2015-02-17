# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testresults', '0006_auto_20150205_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='testexecution',
            name='url',
            field=models.URLField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
