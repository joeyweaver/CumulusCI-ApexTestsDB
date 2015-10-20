import arrow
import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from tokenapi.decorators import token_required
from tokenapi.http import JsonResponse
from tokenapi.http import JsonError

from testresults.forms import TestResultUploadForm
from testresults.models import TestClass
from testresults.models import TestExecution
from testresults.models import TestMethod
from testresults.models import TestResult
from testresults.models import TestCodeUnit
from testresults.importer import STATS_MAP

def testexecutions_list(request):
    executions = TestExecution.objects.all().order_by('-id')
    context = RequestContext(request, {'executions': executions})
    return render_to_response('testresults/testexecutions_list.html', context)

def testexecution_detail(request, execution_id):
    execution = get_object_or_404(TestExecution, id=execution_id)
    data = {'execution': execution}

    last_class = None
    results_by_class = []
    current_class_results = []

    results_query = execution.results.all()

    # Handle configurable display columns
    columns = request.GET.get('columns', 'worst_limit,worst_limit_percent')
    columns = columns.split(',')

    data['columns'] = columns

    # Handle sorting and queryset filtering via GET parameter 'sort'
    sort = request.GET.get('sort', None)
    custom_sort = False
    if sort is None:
        sort = 'method__testclass__name,method__name'
    else:
        custom_sort = True
    sort = sort.split(',')

    results_query = results_query.order_by(*sort)

    if custom_sort:
        for sort_field in sort:
            # Handle stripping '-' from start of sort field to handle DESC sorts
            actual_field = sort_field
            if sort_field.startswith('-'):
                actual_field = sort_field[1:]

            # Ensure that the sort field is not null
            results_query = results_query.filter(**{'%s__isnull' % actual_field: False})

    # Group results by Apex Class for display in template
    for result in results_query:

        # If we're entering a new class, add the last class's results to the results_by_class list
        if result.method.testclass != last_class:
            if current_class_results:
                results_by_class.append({'class': last_class, 'results': current_class_results})
                current_class_results = []

        result_data = {'result': result, 'columns': []}
        for column in columns:
            column_data = {
                'heading': column,
                'value': getattr(result, column),
                'status': 'active',
            }
            percent = None
            if column.find('percent') != -1:
                percent = column_data['value']
            elif column.find('used') != -1:
                percent = getattr(result, column.replace('_used','_percent'))

            if percent is not None:
                if percent < 50:
                    column_data['status'] = 'success'
                elif percent < 70:
                    column_data['status'] = 'info'
                elif percent < 80:
                    column_data['status'] = 'warning'
                else:
                    column_data['status'] = 'danger'
            result_data['columns'].append(column_data)
        current_class_results.append(result_data)
        last_class = result.method.testclass

    # Add the last class's results to the results_by_class list
    if current_class_results:
       results_by_class.append({'class': last_class, 'results': current_class_results})

    data['results_by_class'] = results_by_class
    data['sort'] = sort
    data['custom_sort'] = custom_sort
    data['columns'] = columns


    context = RequestContext(request, data)
    return render_to_response('testresults/testexecution_detail.html', context)

def testexecutions_compare(request, execution1_id, execution2_id):
    execution1 = get_object_or_404(TestExecution, id=execution1_id)
    execution2 = get_object_or_404(TestExecution, id=execution2_id)

    diff = execution1.compare_to([execution2])

    context = {
        'execution1': execution1,
        'execution2': execution2,
        'diff': diff,
    }
    return render_to_response('testresults/testexecution_compare.html', context)

def testresult_detail(request, testresult_id):
    testresult = get_object_or_404(TestResult, id=testresult_id)
    data = {'testresult': testresult}

    context = RequestContext(request, data)
    return render_to_response('testresults/testresult_detail.html', context)

def testclasses_list(request):
    testclasses = TestClass.objects.all()
    return HttpResponse('list of TestClass objects')

def testclass_detail(request, testclass_id):
    testclass = get_object_or_404(TestClass, id=testclass_id)
    return HttpResponse('details of TestClass %s' % testclass_id)

def testmethod_list(request):
    testmethods = TestMethod.objects.all()
    return HttpResponse('list of Method objects')

class AnalyticsIndexView(TemplateView):
    template_name = 'testresults/testmethod_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AnalyticsIndexView, self).get_context_data(**kwargs)

        testmethod_id = kwargs.get('testmethod_id')
        self.testmethod = get_object_or_404(TestMethod, id = testmethod_id)

        context.update(self.get_stats())

        return context

    def get_stats(self):
        final_data = []

        return final_data

def testmethod_detail(request, testmethod_id):
    testmethod = get_object_or_404(TestMethod, id=testmethod_id)

    results = {}
    
    for result in testmethod.results.filter(soql_queries_used__gt = 50).order_by('execution__commit__commit_date'):
        branch = result.execution.branch.name
        commit_date = arrow.get(result.execution.commit.commit_date)
        
        for stat in STATS_MAP.keys():
            used = getattr(result, '%s_used' % stat)
            if used is None:
                continue
            allowed = getattr(result, '%s_allowed' % stat)
            if allowed is None:
                continue

            if stat not in results:
                results[stat] = {}
            if branch not in results[stat]:
                results[stat][branch] = []

            results[stat][branch].append({
                'date': commit_date,
                'used': used,
                'allowed': allowed,
                'percent': (float(used) * 100) / allowed, 
                'result': result,
            })

    context = {}

    for stat, branches in results.items():
        context[stat] = []
        for branch, branch_results in branches.items():
            branch_data = []
            for result in branch_results:
                branch_data.append({'x': result['date'].timestamp, 'y': result['used']})
            context[stat].append({'branch': branch, 'data': json.dumps(branch_data)})

    context['method'] = testmethod

    return render_to_response('testresults/testmethod_detail.html', context, context_instance=RequestContext(request))

def testmethod_metric(request, testmethod_id, metric):
    testmethod = get_object_or_404(TestMethod, id=testmethod_id)

    stats = {}

    for result in testmethod.results.order_by('execution__commit__commit_date', ):
        branch = result.execution.branch.name
        commit_date = result.execution.commit.commit_date

        used = getattr(result, '%s_used' % stat)
        if used is None:
            continue
        allowed = getattr(result, '%s_allowed' % stat)
        if allowed is None:
            continue

        if stat not in context:
            context[stat] = {}
        if branch not in context[stat]:
            context[stat][branch] = []

        stats[branch].append({
            'date': commit_date, 
            'used': used,
            'allowed': allowed,
            'percent': (float(used) * 100) / allowed, 
            'commit': result.execution.commit,
        })

    return HttpResponse(content_type = 'application/json')

@csrf_exempt
@token_required
def upload_test_result(request):

    if request.method == 'POST':
        form = TestResultUploadForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['results_file']
            results = f.read()
            results = json.loads(results)

            repo_url =  form.cleaned_data['repository_url']
            repo_name =  '/'.join(repo_url.split('/')[3:5])
            branch_url = repo_url + '/trees/' + form.cleaned_data['branch_name']
            commit_url = repo_url + '/trees/' + form.cleaned_data['commit_sha']

            test_results = {
                'package': {
                    'name': form.cleaned_data['package'],
                },
                'repository': {
                    'name': repo_name,
                    'url': repo_url,
                },
                'branch': {
                    'name': form.cleaned_data['branch_name'],
                    'url': branch_url,
                },
                'commit': {
                    'name': form.cleaned_data['commit_sha'],
                    'url': commit_url,
                },
                'execution': {
                    'name': form.cleaned_data['execution_name'],
                    'url': form.cleaned_data['execution_url'],
                },
                'environment': {
                    'name': form.cleaned_data['environment_name'],
                },
                'results': results,
            }

            from testresults.importer import import_test_results
            execution = import_test_results(test_results)
            return JsonResponse({'execution_id': execution.id})
    else:
        return JsonError('Only POST is allowed')
        #form = TestResultUploadForm()

    context = RequestContext(request, {'form': form})

    return render_to_response('testresults/upload_test_result.html', context)

