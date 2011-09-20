from django.conf.urls.defaults import patterns, url
from djangorestframework import views
from nodehub.apps.nodes import resources

urlpatterns = patterns('',
    url(r'^$', views.ListOrCreateModelView.as_view(resource=resources.Node)),
    url(r'^/(?P<name>[\w_.-]{1,255})$', views.InstanceModelView.as_view(resource=resources.Node)),
)
