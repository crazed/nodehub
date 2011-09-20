from django.conf.urls.defaults import include, patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    # api
    (r'^api/dns', include('nodehub.apps.dns.urls_api')),
    (r'^api/node', include('nodehub.apps.node.urls_api')),
    # gui
    (r'^dns', include('nodehub.apps.dns.urls')),
    (r'^node', include('nodehub.apps.node.urls')),
)
