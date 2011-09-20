from djangorestframework import resources
from nodehub.apps.node import models

class Host(resources.ModelResource):
    model = models.Host
    fields = ('name', 'url', 'created', 'updated')
