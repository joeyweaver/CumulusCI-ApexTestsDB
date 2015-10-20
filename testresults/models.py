import dateutil.parser
from collections import OrderedDict
from django.db import models
from django import forms
from testresults.choices import OUTCOME_CHOICES
from testresults.github import call_api
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey

class Package(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

    def __unicode__(self):
        return self.name

class Repository(models.Model):
    name = models.CharField(max_length=255)
    package = models.ForeignKey(Package, related_name='repositories')
    url = models.URLField(max_length=255)
    is_fork = models.BooleanField(default=False)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Repositories'

    def __unicode__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    package = models.ForeignKey(Package, related_name='branches')
    repository = models.ForeignKey(Repository, related_name='branches')
    url = models.URLField(max_length=255)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Branches'

    def __unicode__(self):
        return self.name

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

    def __unicode__(self):
        return self.name

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
    
    class Meta:
        verbose_name = 'Test Class'
        verbose_name_plural = 'Test Classes'

    def __unicode__(self):
        return self.name

class TestMethod(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    testclass = models.ForeignKey(TestClass, related_name='methods')

    class Meta:
        verbose_name = 'Test Method'

    def __unicode__(self):
        return self.name

class TestEnvironment(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Test Environment'
        verbose_name_plural = 'Test Environments'

    def __unicode__(self):
        return self.name

class TestExecution(models.Model):
    name = models.CharField(max_length=255)
    environment = models.ForeignKey(TestEnvironment, related_name='testexecutions', null=True, blank=True)
    package = models.ForeignKey(Package, related_name='testexecutions')
    repository = models.ForeignKey(Repository, related_name='testexecutions')
    branch = models.ForeignKey(Branch, related_name='testexecutions')
    commit = models.ForeignKey(Commit, related_name='testexecutions')
    url = models.URLField(max_length=255, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Test Execution'
        verbose_name_plural = 'Test Executions'

    def __unicode__(self):
        return self.name

    def compare_to(self, executions):

        executions = [self] + executions
    
        results = OrderedDict()
        for execution in executions:
            for result in execution.results.all():
                cls = result.method.testclass.name
                method = result.method.name
        
                if not cls in results:
                    results[cls] = OrderedDict()
    
                if not method in results[cls]:
                    results[cls][method] = {}
   
                for limit in result.get_limit_types():
                    limit = limit + '_used'
                    test_limit = 'test_' + limit
    
                    if limit not in results[cls][method]:
                        results[cls][method][limit] = OrderedDict()
                    if test_limit not in results[cls][method]:
                        results[cls][method][test_limit] = OrderedDict()
    
                    results[cls][method][limit][execution.id] = getattr(result, limit)
                    results[cls][method][test_limit][execution.id] = getattr(result, test_limit)

        diff = OrderedDict()
       
        for cls, methods in results.items():
            for method, limits in methods.items():
                for limit, executions in limits.items():
                    # Are any values different between the executions?
                    if len(set(executions.values())) > 1:
                        if not cls in diff:
                            diff[cls] = OrderedDict()
    
                        if not method in diff[cls]:
                            diff[cls][method] = {}

                        if limit not in diff[cls][method]:
                            diff[cls][method][limit] = OrderedDict()

                        diff[cls][method][limit] = executions

        return diff
    

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
    email_invocations_percent = models.IntegerField(null=True, blank=True, db_index=True)
    soql_queries_used = models.IntegerField(null=True, blank=True, db_index=True)
    soql_queries_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    soql_queries_percent = models.IntegerField(null=True, blank=True, db_index=True)
    future_calls_used = models.IntegerField(null=True, blank=True, db_index=True)
    future_calls_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    future_calls_percent = models.IntegerField(null=True, blank=True, db_index=True)
    dml_rows_used = models.IntegerField(null=True, blank=True, db_index=True)
    dml_rows_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    dml_rows_percent = models.IntegerField(null=True, blank=True, db_index=True)
    cpu_time_used = models.IntegerField(null=True, blank=True, db_index=True)
    cpu_time_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    cpu_time_percent = models.IntegerField(null=True, blank=True, db_index=True)
    query_rows_used = models.IntegerField(null=True, blank=True, db_index=True)
    query_rows_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    query_rows_percent = models.IntegerField(null=True, blank=True, db_index=True)
    dml_statements_used = models.IntegerField(null=True, blank=True, db_index=True)
    dml_statements_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    dml_statements_percent = models.IntegerField(null=True, blank=True, db_index=True)
    mobile_apex_push_used = models.IntegerField(null=True, blank=True, db_index=True)
    mobile_apex_push_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    mobile_apex_push_percent = models.IntegerField(null=True, blank=True, db_index=True)
    heap_size_used = models.IntegerField(null=True, blank=True, db_index=True)
    heap_size_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    heap_size_percent = models.IntegerField(null=True, blank=True, db_index=True)
    sosl_queries_used = models.IntegerField(null=True, blank=True, db_index=True)
    sosl_queries_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    sosl_queries_percent = models.IntegerField(null=True, blank=True, db_index=True)
    queueable_jobs_used = models.IntegerField(null=True, blank=True, db_index=True)
    queueable_jobs_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    queueable_jobs_percent = models.IntegerField(null=True, blank=True, db_index=True)
    callouts_used = models.IntegerField(null=True, blank=True, db_index=True)
    callouts_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    callouts_percent = models.IntegerField(null=True, blank=True, db_index=True)
    test_email_invocations_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_email_invocations_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_email_invocations_percent = models.IntegerField(null=True, blank=True, db_index=True)
    test_soql_queries_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_soql_queries_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_soql_queries_percent = models.IntegerField(null=True, blank=True, db_index=True)
    test_future_calls_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_future_calls_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_future_calls_percent = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_rows_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_rows_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_rows_percent = models.IntegerField(null=True, blank=True, db_index=True)
    test_cpu_time_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_cpu_time_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_cpu_time_percent = models.IntegerField(null=True, blank=True, db_index=True)
    test_query_rows_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_query_rows_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_query_rows_percent = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_statements_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_statements_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_dml_statements_percent = models.IntegerField(null=True, blank=True, db_index=True)
    test_mobile_apex_push_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_mobile_apex_push_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_mobile_apex_push_percent = models.IntegerField(null=True, blank=True, db_index=True)
    test_heap_size_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_heap_size_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_heap_size_percent = models.IntegerField(null=True, blank=True, db_index=True)
    test_sosl_queries_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_sosl_queries_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_sosl_queries_percent = models.IntegerField(null=True, blank=True, db_index=True)
    test_queueable_jobs_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_queueable_jobs_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_queueable_jobs_percent = models.IntegerField(null=True, blank=True, db_index=True)
    test_callouts_used = models.IntegerField(null=True, blank=True, db_index=True)
    test_callouts_allowed = models.IntegerField(null=True, blank=True, db_index=True)
    test_callouts_percent = models.IntegerField(null=True, blank=True, db_index=True)
    worst_limit = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    worst_limit_percent = models.IntegerField(null=True, blank=True, db_index=True)
    worst_limit_nontest = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    worst_limit_nontest_percent = models.IntegerField(null=True, blank=True, db_index=True)
    worst_limit_test = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    worst_limit_test_percent = models.IntegerField(null=True, blank=True, db_index=True)

    objects = TestResultManager()

    class Meta:
        verbose_name = 'Test Result'
        verbose_name_plural = 'Test Results'

    def __unicode__(self):
        return '%s.%s' % (self.method.testclass, self.method.name)

    def get_main_code_unit(self):
        code_units = self.codeunits.filter(unit_type = 'Test Method')
        if not code_units:
            return None
        return code_units[0]

    def get_limit_types(self):
        types = (
            'email_invocations',
            'soql_queries',
            'future_calls',
            'dml_rows',
            'cpu_time',
            'query_rows',
            'dml_statements',
            'mobile_apex_push',
            'heap_size',
            'sosl_queries',
            'queueable_jobs',
            'callouts',
        )

        return types
    

    def populate_limit_fields(self):
        code_unit = self.get_main_code_unit()

        if not code_unit:
            return None

        limit_types = self.get_limit_types()

        for limit_type in limit_types:
            used = getattr(code_unit, '%s_used' % limit_type)
            allowed = getattr(code_unit, '%s_allowed' % limit_type)
            test_used = getattr(code_unit, 'test_%s_used' % limit_type)
            test_allowed = getattr(code_unit, 'test_%s_allowed' % limit_type)
            percent = None
            test_percent = None

            if used is not None and allowed:
                percent = (used * 100) / allowed
                
            if test_used is not None and test_allowed:
                test_percent = (test_used * 100) / test_allowed
            
            setattr(self, '%s_used' % limit_type, used)
            setattr(self, '%s_allowed' % limit_type, allowed)
            setattr(self, '%s_percent' % limit_type, percent)
            setattr(self, 'test_%s_used' % limit_type,  test_used)
            setattr(self, 'test_%s_allowed' % limit_type, test_allowed)
            setattr(self, 'test_%s_percent' % limit_type, test_percent)

        worst_limit = None
        worst_limit_percent = None
        worst_limit_nontest = None
        worst_limit_nontest_percent = None
        worst_limit_test = None
        worst_limit_test_percent = None

        for limit_type in limit_types:
            percent_nontest = getattr(self, '%s_percent' % limit_type)
            percent_test = getattr(self, 'test_%s_percent' % limit_type)

            if percent_nontest > worst_limit_percent:
                worst_limit = '%s_percent' % limit_type
                worst_limit_percent = percent_nontest
            if percent_nontest > worst_limit_nontest_percent:
                worst_limit_nontest = '%s_percent' % limit_type
                worst_limit_nontest_percent = percent_nontest

            if percent_test > worst_limit_percent:
                worst_limit = 'test_%s_percent' % limit_type
                worst_limit_percent = percent_test
            if percent_test > worst_limit_test_percent:
                worst_limit_test = 'test_%s_percent' % limit_type
                worst_limit_test_percent = percent_test

        self.worst_limit = worst_limit
        self.worst_limit_percent = worst_limit_percent
        self.worst_limit_nontest = worst_limit_nontest
        self.worst_limit_nontest_percent = worst_limit_nontest_percent
        self.worst_limit_test = worst_limit_test
        self.worst_limit_test_percent = worst_limit_test_percent

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

    class Meta:
        verbose_name = 'Test Code Unit'
        verbose_name_plural = 'Test Code Units'

    def __unicode__(self):
        return '[%s] - %s' % (self.unit_type, self.unit)
