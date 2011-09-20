from django.core.urlresolvers import reverse
from djangorestframework import resources
from nodehub.apps.dns import models

class Zone(resources.ModelResource):
    model = models.Zone
    fields = ('name', 'ttl', 'records', 'url')

    def records(self, instance):
        return reverse('records_api', kwargs={'zone__name': instance.name})

class Record(resources.ModelResource):
    model = models.Record
    fields = ('name', 'type', 'content', 'priority', 'ttl', 'zone', 'url')

    def zone(self, instance):
        return reverse('zone_api', kwargs={'name': instance.zone.name})

    def url(self, instance):
        return reverse('record_api', kwargs={'zone__name': instance.zone.name, 'id': instance.pk})
