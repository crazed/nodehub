from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^/hosts/(?P<name>[\w_.-]{1,255})$', 'nodehub.apps.node.views.host_detail'),
)
