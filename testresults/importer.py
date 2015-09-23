from testresults.models import *

STATS_MAP = {
    'email_invocations': 'Number of Email Invocations',
    'soql_queries': 'Number of SOQL queries',
    'future_calls': 'Number of future calls',
    'dml_rows': 'Number of DML rows',
    'cpu_time': 'Maximum CPU time',
    'query_rows': 'Number of query rows',
    'dml_statements': 'Number of DML statements',
    'mobile_apex_push': 'Number of Mobile Apex push calls',
    'heap_size': 'Maximum heap size',
    'sosl_queries': 'Number of SOSL queries',
    'queueable_jobs': 'Number of queueable jobs added to the queue',
    'callouts': 'Number of callouts',
    'test_email_invocations': 'TESTING_LIMITS: Number of Email Invocations',
    'test_soql_queries': 'TESTING_LIMITS: Number of SOQL queries',
    'test_future_calls': 'TESTING_LIMITS: Number of future calls',
    'test_dml_rows': 'TESTING_LIMITS: Number of DML rows',
    'test_cpu_time': 'TESTING_LIMITS: Maximum CPU time',
    'test_query_rows': 'TESTING_LIMITS: Number of query rows',
    'test_dml_statements': 'TESTING_LIMITS: Number of DML statements',
    'test_mobile_apex_push': 'TESTING_LIMITS: Number of Mobile Apex push calls',
    'test_heap_size': 'TESTING_LIMITS: Maximum heap size',
    'test_sosl_queries': 'TESTING_LIMITS: Number of SOSL queries',
    'test_queueable_jobs': 'TESTING_LIMITS: Number of queueable jobs added to the queue',
    'test_callouts': 'TESTING_LIMITS: Number of callouts',
}

def import_test_results(results):
    classes = {}
    methods = {}

    package_url = results['package'].get('url', None)
    if not package_url:
        package_url = results['repository']['url']

    package, created = Package.objects.get_or_create(
        name = results['package']['name'],
        url = package_url,
    )

    repository, created = Repository.objects.get_or_create(
        name = results['repository']['name'],
        url = results['repository']['url'],
        package = package,
    )

    branch, created = Branch.objects.get_or_create(
        name = results['branch']['name'],
        url = results['branch']['url'],
        package = package,
        repository = repository,
    )

    commit, created = Commit.objects.get_or_create(
        name = results['commit']['name'],
        url = results['commit']['url'],
        package = package,
        repository = repository,
        branch = branch,
    )

    environment, created = TestEnvironment.objects.get_or_create(
        name = results['environment']['name'],
    )

    execution = TestExecution(
        name = results['execution']['name'],
        url = results['execution']['url'],
        package = package,
        repository = repository,
        branch = branch,
        commit = commit,
        environment = environment,
    )
    execution.save()

    for result in results['results']:
        class_and_method = '%s.%s' % (result['ClassName'], result['Method'])

        testclass = classes.get(result['ClassName'], None)
        if not testclass:
            try:
                testclass = TestClass.objects.get(name = result['ClassName'], package=commit.package.id)
            except TestClass.DoesNotExist:
                testclass = TestClass(name = result['ClassName'], package=commit.package)
                testclass.save()
            classes[result['ClassName']] = testclass

        method = methods.get(class_and_method, None)
        if not method:
            try:
                method = TestMethod.objects.get(testclass = testclass.id, name = result['Method'])
            except TestMethod.DoesNotExist:
                method = TestMethod(testclass = testclass, name = result['Method'])
                method.save()
            methods[result['Method']] = method

        duration = None
        if 'Stats' in result and result['Stats'] and 'duration' in result['Stats'] and result['Stats']['duration']:
            duration = result['Stats']['duration']
       
        testresult = TestResult(
            execution = execution,
            method = method,
            duration = duration,
            outcome = result['Outcome'],
            stacktrace = result['StackTrace'],
            message = result['Message'],
        ) 
        testresult.save()

        if 'Stats' in result and result['Stats']:
            testcodeunit = TestCodeUnit(
                testresult = testresult,
                unit = result['Method'],
                unit_type = 'Test Method',
            )
            for stat in STATS_MAP.keys():
                used = '%s_used' % stat
                setattr(testcodeunit, used, get_value_from_stats(result['Stats'], used))
                allowed = '%s_allowed' % stat
                setattr(testcodeunit, allowed, get_value_from_stats(result['Stats'], allowed))

            testcodeunit.save()

        if 'Children' in result and result['Children']:
            process_children(result['Children'], testresult, testcodeunit)

        testresult.populate_limit_fields()

    return execution

def process_children(children, testresult, parent):
    if not children:
        return

    for child in children:
        testcodeunit = TestCodeUnit(
            testresult = testresult,
            parent = parent,
            unit = child['unit'],
            unit_type = child['unit_type'],
            duration = child['stats'].get('duration', None)
        )

        for stat in STATS_MAP.keys():
            used = '%s_used' % stat
            setattr(testcodeunit, used, get_value_from_stats(child['stats'], used))
            allowed = '%s_allowed' % stat
            setattr(testcodeunit, allowed, get_value_from_stats(child['stats'], allowed))

        if 'unit_info' in child and child['unit_info']:
            testcodeunit.sobject = child['unit_info'].get('object')
            testcodeunit.event = child['unit_info'].get('event')

        testcodeunit.save()

        if child['children']:
            process_children(child['children'], testresult, testcodeunit)
            

def get_value_from_stats(stats, field):
    if not stats:
        return

    field_parts = field.split('_')
    suffix = field_parts[-1]
    key = '_'.join(field_parts[0:-1])
    stats_key = STATS_MAP.get(key)
    
    if stats_key not in stats:
        return

    value = stats[stats_key][suffix]
    value = value.replace(' ******* CLOSE TO LIMIT', '')
    return int(value)
        
    
        
    
