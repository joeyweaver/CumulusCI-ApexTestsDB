# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestCodeUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.TextField()),
                ('unit_type', models.CharField(max_length=255)),
                ('duration', models.FloatField(null=True, blank=True)),
                ('event', models.CharField(max_length=255, null=True, blank=True)),
                ('sobject', models.CharField(max_length=255, null=True, blank=True)),
                ('email_invocations_used', models.IntegerField()),
                ('email_invocations_allowed', models.IntegerField()),
                ('soql_queries_used', models.IntegerField()),
                ('soql_queries_allowed', models.IntegerField()),
                ('future_calls_used', models.IntegerField()),
                ('future_calls_allowed', models.IntegerField()),
                ('dml_rows_used', models.IntegerField()),
                ('dml_rows_allowed', models.IntegerField()),
                ('cpu_time_used', models.IntegerField()),
                ('cpu_time_allowed', models.IntegerField()),
                ('query_rows_used', models.IntegerField()),
                ('query_rows_allowed', models.IntegerField()),
                ('dml_statements_used', models.IntegerField()),
                ('dml_statements_allowed', models.IntegerField()),
                ('mobile_apex_push_used', models.IntegerField()),
                ('mobile_apex_push_allowed', models.IntegerField()),
                ('heap_size_used', models.IntegerField()),
                ('heap_size_allowed', models.IntegerField()),
                ('sosl_queries_used', models.IntegerField()),
                ('sosl_queries_allowed', models.IntegerField()),
                ('queueable_jobs_used', models.IntegerField()),
                ('queueable_jobs_allowed', models.IntegerField()),
                ('callouts_used', models.IntegerField()),
                ('callouts_allowed', models.IntegerField()),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='testresults.TestCodeUnit', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestExecution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('branch', models.ForeignKey(related_name='branches', to='testresults.Branch')),
                ('commit', models.ForeignKey(related_name='commits', to='testresults.Branch')),
                ('repository', models.ForeignKey(related_name='repositories', to='testresults.Repository')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('testclass', models.ForeignKey(related_name='methods', to='testresults.TestClass')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('duration', models.FloatField()),
                ('outcome', models.CharField(max_length=16, choices=[(b'Pass', b'Pass'), (b'CompileFail', b'CompileFail'), (b'Fail', b'Fail'), (b'Skip', b'Skip')])),
                ('stacktrace', models.TextField(null=True, blank=True)),
                ('message', models.TextField(null=True, blank=True)),
                ('execution', models.ForeignKey(related_name='results', to='testresults.TestExecution')),
                ('method', models.ForeignKey(related_name='results', to='testresults.TestMethod')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='testcodeunit',
            name='testresult',
            field=models.ForeignKey(related_name='codeunits', to='testresults.TestResult'),
            preserve_default=True,
        ),
    ]
