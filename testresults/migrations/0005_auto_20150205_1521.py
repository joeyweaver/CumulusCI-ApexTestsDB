# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testresults', '0004_auto_20150205_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='branch',
            name='is_default',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='branch',
            name='package',
            field=models.ForeignKey(related_name='branches', default=0, to='testresults.Package'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='repository',
            field=models.ForeignKey(related_name='branches', default=0, to='testresults.Repository'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='url',
            field=models.URLField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commit',
            name='branch',
            field=models.ForeignKey(related_name='commits', default=0, to='testresults.Branch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commit',
            name='package',
            field=models.ForeignKey(related_name='commits', default=0, to='testresults.Package'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commit',
            name='repository',
            field=models.ForeignKey(related_name='commits', default=0, to='testresults.Repository'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commit',
            name='url',
            field=models.URLField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repository',
            name='is_fork',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='repository',
            name='package',
            field=models.ForeignKey(related_name='repositories', default=0, to='testresults.Package'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repository',
            name='url',
            field=models.URLField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testclass',
            name='package',
            field=models.ForeignKey(related_name='testclasses', default=0, to='testresults.Repository'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testexecution',
            name='branch',
            field=models.ForeignKey(related_name='testexecutions', to='testresults.Branch'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testexecution',
            name='commit',
            field=models.ForeignKey(related_name='testexecutions', to='testresults.Commit'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testexecution',
            name='repository',
            field=models.ForeignKey(related_name='testexecutions', to='testresults.Repository'),
            preserve_default=True,
        ),
    ]
