from django.conf.urls.defaults import include, patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^api/nodes', include('nodehub.apps.nodes.urls_api')),
    (r'^', include('nodehub.apps.nodes.urls')),
)
