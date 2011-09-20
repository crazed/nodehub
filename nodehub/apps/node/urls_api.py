from django.conf.urls.defaults import patterns, url
from djangorestframework import views
from nodehub.apps.node import resources

urlpatterns = patterns('',
    url(r'^/hosts$', views.ListOrCreateModelView.as_view(resource=resources.Host)),
    url(r'^/hosts/(?P<name>[\w_.-]{1,255})$', views.InstanceModelView.as_view(resource=resources.Host)),
)
