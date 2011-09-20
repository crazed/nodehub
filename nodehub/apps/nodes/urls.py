from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^nodes/(?P<name>[\w_.-]{1,255})$', 'nodehub.apps.nodes.views.node_detail'),
)
