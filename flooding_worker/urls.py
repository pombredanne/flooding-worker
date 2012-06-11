# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf import settings
from django.conf.urls.defaults import handler404
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin
from django.http import HttpResponseServerError
from django.template import Context
from django.template import loader

admin.autodiscover()
handler404  # pyflakes

urlpatterns = patterns(
    '',
    url(r'^log/$', 'lizard_flooding_worker.views.homepage',
        name='lizard_flooding_worker.homepage'),
    url(r'^log/customer/(?P<customer_id>\d+)/$',
     'lizard_flooding_worker.views.homepage',
        name='lizard_flooding_worker-workflows'),
    url(r'^log/customer/(?P<customer_id>\d+)/workflow/(?P<workflow_id>\d+)/$',
     'lizard_flooding_worker.views.homepage',
        name='lizard_flooding_worker-loggings'),
    (r'^admin/', include(admin.site.urls)),
    )


if settings.DEBUG:
    # Add this also to the projects that use this application
    urlpatterns += patterns('',
        (r'', include('staticfiles.urls')),
    )


def handler500(request):
    """500 error handler which includes ``request`` in the context.

    Simple test:

      >>> handler500({})  #doctest: +ELLIPSIS
      <django.http.HttpResponseServerError object at ...>

    """
    t = loader.get_template('500.html')
    return HttpResponseServerError(
        t.render(Context({'request': request})))