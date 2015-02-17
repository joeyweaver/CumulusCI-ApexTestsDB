# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testresults', '0007_testexecution_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testclass',
            name='package',
            field=models.ForeignKey(related_name='testclasses', to='testresults.Package'),
            preserve_default=True,
        ),
    ]
