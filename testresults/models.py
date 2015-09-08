import dateutil.parser
from django.db import models
from django import forms
from testresults.choices import OUTCOME_CHOICES
from testresults.github import call_api
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey

class Package(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

class Repository(models.Model):
    name = models.CharField(max_length=255)
    package = models.ForeignKey(Package, related_name='repositories')
    url = models.URLField(max_length=255)
    is_fork = models.BooleanField(default=False)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

class Branch(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    package = models.ForeignKey(Package, related_name='branches')
    repository = models.ForeignKey(Repository, related_name='branches')
    url = models.URLField(max_length=255)
    is_default = models.BooleanField(default=False)

class CommitManager(models.Manager):

    def update_commit_dates(self, replace=None):
        if replace:
            commits = self.all()
        else:
            commits = self.filter(commit_date__isnull = True)
        for commit in commits:
            commit.update_commit_date()
   
class Commit(models.Model):
    name = models.CharField(max_length=255, db_index=True) 
    package = models.ForeignKey(Package, related_name='commits')
    repository = models.ForeignKey(Repository, related_name='commits')
    branch = models.ForeignKey(Branch, related_name='commits')
    commit_date = models.DateTimeField(null=True, blank=True)
    url = models.URLField(max_length=255)

    objects = CommitManager()

    def update_commit_date(self):
        repo_owner, repo_name = commit.repository.name.split('/')
        resp = call_api(
            repo_owner, 
            repo_name, 
            '/commits/%s' % commit.name, 
            username=commit.repository.username, 
            password=commit.repository.password
        )
        commit_date = resp['commit']['committer']['date']
        commit_date = dateutil.parser.parse(commit_date)
        commit.commit_date = commit_date
        commit.save()

class TestClass(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    package = models.ForeignKey(Package, related_name='testclasses')
    
class TestMethod(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    testclass = models.ForeignKey(TestClass, related_name='methods')

class TestExecution(models.Model):
    name = models.CharField(max_length=255)
    package = models.ForeignKey(Package, related_name='testexecutions')
    repository = models.ForeignKey(Repository, related_name='testexecutions')
    branch = models.ForeignKey(Branch, related_name='testexecutions')
    commit = models.ForeignKey(Commit, related_name='testexecutions')
    url = models.URLField(max_length=255, null=True, blank=True)

class TestResultManager(models.Manager):
    def update_summary_fields(self):
        for summary in self.all():
            summary.update_summary_fields()

class TestResult(models.Model):
    execution = models.ForeignKey(TestExecution, related_name='results')
    method = models.ForeignKey(TestMethod, related_name='results')
    duration = models.FloatField(null=True, blank=True, db_index=True)
    outcome = models.CharField(max_length=16, choices=OUTCOME_CHOICES, db_index=True)
    stacktrace = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    email_invocations_used = models.IntegerField(null=True, blank=True, db_index=True)
    email_invocations_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    soql_queries_used = models.IntegerField(null=True, blank=True, db_index=True)
    soql_queries_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    future_calls_used = models.IntegerField(null=True, blank=True, db_index=True)
    future_calls_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    dml_rows_used = models.IntegerField(null=True, blank=True, db_index=True)
    dml_rows_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    cpu_time_used = models.IntegerField(null=True, blank=True, db_index=True)
    cpu_time_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    query_rows_used = models.IntegerField(null=True, blank=True, db_index=True)
    query_rows_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    dml_statements_used = models.IntegerField(null=True, blank=True, db_index=True)
    dml_statements_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    mobile_apex_push_used = models.IntegerField(null=True, blank=True, db_index=True)
    mobile_apex_push_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    heap_size_used = models.IntegerField(null=True, blank=True, db_index=True)
    heap_size_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    sosl_queries_used = models.IntegerField(null=True, blank=True, db_index=True)
    sosl_queries_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    queueable_jobs_used = models.IntegerField(null=True, blank=True, db_index=True)
    queueable_jobs_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    callouts_used = models.IntegerField(null=True, blank=True, db_index=True)
    callouts_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_email_invocations_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_email_invocations_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_soql_queries_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_soql_queries_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_future_calls_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_future_calls_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_rows_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_rows_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_cpu_time_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_cpu_time_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_query_rows_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_query_rows_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_statements_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_statements_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_mobile_apex_push_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_mobile_apex_push_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_heap_size_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_heap_size_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_sosl_queries_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_sosl_queries_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_queueable_jobs_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_queueable_jobs_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_callouts_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_callouts_allowed = models.IntegerField(null=True, blank=True, db_index=True)

    objects = TestResultManager()

    def __unicode__(self):
        return '%s.%s' % (self.method.testclass, self.method.name)

    def get_main_code_unit(self):
        code_units = self.codeunits.filter(unit_type = 'Test Method')
        if not code_units:
            return None
        return code_units[0]

    def update_summary_fields(self):
        limits = self.codeunits.aggregate(
            models.Count('id'),
            models.Sum('email_invocations_used'),
            models.Sum('soql_queries_used'),
            models.Sum('future_calls_used'),
            models.Sum('dml_rows_used'),
            models.Sum('cpu_time_used'),
            models.Sum('query_rows_used'),
            models.Sum('dml_statements_used'),
            models.Sum('mobile_apex_push_used'),
            models.Sum('heap_size_used'),
            models.Sum('sosl_queries_used'),
            models.Sum('queueable_jobs_used'),
            models.Sum('callouts_used'),
        )

        if not limits['id__count']:
            return

        codeunit = self.codeunits.all()[0]
        self.email_invocations_allowed = codeunit.email_invocations_allowed
        self.soql_queries_allowed = codeunit.soql_queries_allowed
        self.future_calls_allowed = codeunit.future_calls_allowed
        self.dml_rows_allowed = codeunit.dml_rows_allowed
        self.cpu_time_allowed = codeunit.cpu_time_allowed
        self.query_rows_allowed = codeunit.query_rows_allowed
        self.dml_statements_allowed = codeunit.dml_statements_allowed
        self.mobile_apex_push_allowed = codeunit.mobile_apex_push_allowed
        self.heap_size_allowed = codeunit.heap_size_allowed
        self.sosl_queries_allowed = codeunit.sosl_queries_allowed
        self.queueable_jobs_allowed = codeunit.queueable_jobs_allowed
        self.callouts_allowed = codeunit.callouts_allowed

        self.email_invocations_used = limits['email_invocations_used__sum']
        self.soql_queries_used = limits['soql_queries_used__sum']
        self.future_calls_used = limits['future_calls_used__sum']
        self.dml_rows_used = limits['dml_rows_used__sum']
        self.cpu_time_used = limits['cpu_time_used__sum']
        self.query_rows_used = limits['query_rows_used__sum']
        self.dml_statements_used = limits['dml_statements_used__sum']
        self.mobile_apex_push_used = limits['mobile_apex_push_used__sum']
        self.heap_size_used = limits['heap_size_used__sum']
        self.sosl_queries_used = limits['sosl_queries_used__sum']
        self.queueable_jobs_used = limits['queueable_jobs_used__sum']
        self.callouts_used = limits['callouts_used__sum']
        
        self.save()

class TestCodeUnit(MPTTModel):
    testresult = models.ForeignKey(TestResult, related_name='codeunits')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    unit = models.TextField(db_index=True)
    unit_type = models.CharField(max_length=255, db_index=True)
    duration = models.FloatField(null=True, blank=True, db_index=True)
    event = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    sobject = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    email_invocations_used = models.IntegerField(null=True, blank=True, db_index=True)
    email_invocations_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    soql_queries_used = models.IntegerField(null=True, blank=True, db_index=True)
    soql_queries_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    future_calls_used = models.IntegerField(null=True, blank=True, db_index=True)
    future_calls_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    dml_rows_used = models.IntegerField(null=True, blank=True, db_index=True)
    dml_rows_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    cpu_time_used = models.IntegerField(null=True, blank=True, db_index=True)
    cpu_time_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    query_rows_used = models.IntegerField(null=True, blank=True, db_index=True)
    query_rows_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    dml_statements_used = models.IntegerField(null=True, blank=True, db_index=True)
    dml_statements_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    mobile_apex_push_used = models.IntegerField(null=True, blank=True, db_index=True)
    mobile_apex_push_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    heap_size_used = models.IntegerField(null=True, blank=True, db_index=True)
    heap_size_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    sosl_queries_used = models.IntegerField(null=True, blank=True, db_index=True)
    sosl_queries_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    queueable_jobs_used = models.IntegerField(null=True, blank=True, db_index=True)
    queueable_jobs_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    callouts_used = models.IntegerField(null=True, blank=True, db_index=True)
    callouts_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_email_invocations_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_email_invocations_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_soql_queries_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_soql_queries_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_future_calls_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_future_calls_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_rows_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_rows_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_cpu_time_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_cpu_time_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_query_rows_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_query_rows_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_statements_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_statements_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_mobile_apex_push_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_mobile_apex_push_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_heap_size_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_heap_size_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_sosl_queries_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_sosl_queries_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_queueable_jobs_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_queueable_jobs_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_callouts_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_callouts_allowed = models.IntegerField(null=True, blank=True, db_index=True)

    #class MPTTMeta:
    #    order_insertion_by = ['id']

    def __unicode__(self):
        return '[%s] - %s' % (self.unit_type, self.unit)
