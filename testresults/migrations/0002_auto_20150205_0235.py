# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testresults', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testexecution',
            name='commit',
            field=models.ForeignKey(related_name='commits', to='testresults.Commit'),
            preserve_default=True,
        ),
    ]
