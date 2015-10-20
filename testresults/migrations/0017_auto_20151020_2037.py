# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testresults', '0016_auto_20150923_1944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name_plural': 'Branches'},
        ),
        migrations.AlterModelOptions(
            name='repository',
            options={'verbose_name_plural': 'Repositories'},
        ),
        migrations.AlterModelOptions(
            name='testclass',
            options={'verbose_name': 'Test Class', 'verbose_name_plural': 'Test Classes'},
        ),
        migrations.AlterModelOptions(
            name='testcodeunit',
            options={'verbose_name': 'Test Code Unit', 'verbose_name_plural': 'Test Code Units'},
        ),
        migrations.AlterModelOptions(
            name='testenvironment',
            options={'verbose_name': 'Test Environment', 'verbose_name_plural': 'Test Environments'},
        ),
        migrations.AlterModelOptions(
            name='testexecution',
            options={'verbose_name': 'Test Execution', 'verbose_name_plural': 'Test Executions'},
        ),
        migrations.AlterModelOptions(
            name='testmethod',
            options={'verbose_name': 'Test Method'},
        ),
        migrations.AlterModelOptions(
            name='testresult',
            options={'verbose_name': 'Test Result', 'verbose_name_plural': 'Test Results'},
        ),
        migrations.AddField(
            model_name='testexecution',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 20, 20, 37, 27, 989613, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
