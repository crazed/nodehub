from djangorestframework import resources
from nodehub.apps.nodes import models

class Node(resources.ModelResource):
    model = models.Node
