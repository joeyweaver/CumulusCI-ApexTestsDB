# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testresults', '0012_auto_20150831_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcodeunit',
            name='test_callouts_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_callouts_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_cpu_time_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_cpu_time_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_dml_rows_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_dml_rows_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_dml_statements_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_dml_statements_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_email_invocations_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_email_invocations_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_future_calls_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_future_calls_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_heap_size_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_heap_size_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_mobile_apex_push_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_mobile_apex_push_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_query_rows_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_query_rows_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_queueable_jobs_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_queueable_jobs_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_soql_queries_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_soql_queries_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_sosl_queries_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='test_sosl_queries_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
