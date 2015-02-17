from django.conf.urls import patterns, url

urlpatterns = patterns('',
#    url(r'^packages$', 'testresults.views.packages_list'),
#    url(r'^packages/(?P<package_id>[0-9]+)$', 'testresults.views.package_detail'),
#    url(r'^repositories$', 'testresults.views.repositories_list'),
#    url(r'^repositories/(?P<repository_id>[0-9]+)$', 'testresults.views.repository_detail'),
#    url(r'^branches$', 'testresults.views.branches_list'),
#    url(r'^branches/(?P<branch_id>[0-9]+)$', 'testresults.views.branch_detail'),
#    url(r'^commits$', 'testresults.views.commits_list'),
#    url(r'^commits/(?P<commit_id>[0-9]+)$', 'testresults.views.commit_detail'),
#    url(r'^executions$', 'testresults.views.executions_list'),
#    url(r'^executions/(?P<execution_id>[0-9]+)$', 'testresults.views.execution_detail'),
    url(r'^testclasses$', 'testresults.views.testclasses_list'),
    url(r'^testclasses/(?P<testclass_id>[0-9]+)$', 'testresults.views.testclass_detail'),
#    url(r'^testclasses/(?P<testclass_id>[0-9]+)/execution/(?P<execution_id>[0-9]+)$', 'testresults.views.testclass_execution_detail'),
    url(r'^testmethods$', 'testresults.views.testmethods_list'),
    url(r'^testmethods/(?P<testmethod_id>[0-9]+)$', 'testresults.views.testmethod_detail'),
#    url(r'^methods/(?P<testclass_id>[0-9]+)/execution/(?P<execution_id>[0-9]+)$', 'testresults.views.testclass_execution_detail'),

)
