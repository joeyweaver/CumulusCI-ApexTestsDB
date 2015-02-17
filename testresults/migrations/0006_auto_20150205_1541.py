# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testresults', '0005_auto_20150205_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='testexecution',
            name='package',
            field=models.ForeignKey(related_name='testexecutions', default=0, to='testresults.Package'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(max_length=255, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='commit',
            name='name',
            field=models.CharField(max_length=255, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testclass',
            name='name',
            field=models.CharField(max_length=255, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='callouts_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='callouts_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='cpu_time_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='cpu_time_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='dml_rows_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='dml_rows_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='dml_statements_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='dml_statements_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='duration',
            field=models.FloatField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='email_invocations_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='email_invocations_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='event',
            field=models.CharField(db_index=True, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='future_calls_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='future_calls_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='heap_size_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='heap_size_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='mobile_apex_push_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='mobile_apex_push_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='query_rows_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='query_rows_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='queueable_jobs_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='queueable_jobs_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='sobject',
            field=models.CharField(db_index=True, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='soql_queries_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='soql_queries_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='sosl_queries_allowed',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='sosl_queries_used',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='unit',
            field=models.TextField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testcodeunit',
            name='unit_type',
            field=models.CharField(max_length=255, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testmethod',
            name='name',
            field=models.CharField(max_length=255, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testresult',
            name='duration',
            field=models.FloatField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testresult',
            name='outcome',
            field=models.CharField(db_index=True, max_length=16, choices=[(b'Pass', b'Pass'), (b'CompileFail', b'CompileFail'), (b'Fail', b'Fail'), (b'Skip', b'Skip')]),
            preserve_default=True,
        ),
    ]
