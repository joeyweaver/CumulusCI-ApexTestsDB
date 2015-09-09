# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testresults', '0013_auto_20150831_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='callouts_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='cpu_time_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='dml_rows_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='dml_statements_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='email_invocations_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='future_calls_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='heap_size_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='mobile_apex_push_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='query_rows_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='queueable_jobs_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='soql_queries_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='sosl_queries_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_callouts_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_cpu_time_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_dml_rows_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_dml_statements_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_email_invocations_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_future_calls_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_heap_size_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_mobile_apex_push_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_query_rows_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_queueable_jobs_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_soql_queries_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_sosl_queries_percent',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
