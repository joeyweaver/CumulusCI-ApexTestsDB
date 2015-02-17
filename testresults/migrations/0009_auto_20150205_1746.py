# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testresults', '0008_auto_20150205_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='callouts_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='callouts_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='cpu_time_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='cpu_time_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='dml_rows_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='dml_rows_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='dml_statements_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='dml_statements_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='email_invocations_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='email_invocations_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='future_calls_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='future_calls_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='heap_size_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='heap_size_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='mobile_apex_push_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='mobile_apex_push_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='query_rows_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='query_rows_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='queueable_jobs_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='queueable_jobs_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='soql_queries_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='soql_queries_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='sosl_queries_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='sosl_queries_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
