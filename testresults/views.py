import arrow
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from testresults.models import TestClass
from testresults.models import TestMethod
from testresults.models import TestCodeUnit
from testresults.importer import STATS_MAP

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
