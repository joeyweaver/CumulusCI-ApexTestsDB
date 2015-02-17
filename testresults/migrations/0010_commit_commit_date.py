# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testresults', '0009_auto_20150205_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='commit_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
