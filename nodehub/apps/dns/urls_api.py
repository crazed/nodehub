from django.conf.urls.defaults import patterns, url
from djangorestframework import views
from nodehub.apps.dns import resources

urlpatterns = patterns('',
    url(r'^/zones$', views.ListOrCreateModelView.as_view(resource=resources.Zone), name='zones_api'),
    url(r'^/zones/(?P<name>[\w_.-]{1,255})$', views.InstanceModelView.as_view(resource=resources.Zone), name='zone_api'),
    url(r'^/zones/(?P<zone__name>[\w_.-]{1,255})/records$', views.InstanceModelView.as_view(resource=resources.Record), name='records_api'),
    url(r'^/zones/(?P<zone__name>[\w_.-]{1,255})/records/(?P<id>\d)$', views.InstanceModelView.as_view(resource=resources.Record), name='record_api'),
)
