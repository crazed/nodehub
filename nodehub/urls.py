from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    # api
    (r'^api/nodes/(?P<name>[\w_.-]{1,255})$', 'nodehub.apps.nodes.views.get'),
    (r'^api/nodes/(?P<name>[\w_.-]{1,255})/render$', 'nodehub.apps.nodes.views.render'),
)
