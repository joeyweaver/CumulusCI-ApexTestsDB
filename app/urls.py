from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('testresults.urls')),
    url(r'', include('tokenapi.urls')),
    url(r'^django-rq/', include('django_rq.urls')),
)
