from nodehub.apps.nodes import models

class Error(Exception): pass
class NotFound(Error): pass

class Node(object):

    def __init__(self, name):
        try:
            self.model = models.Node.objects.get(name=name)
        except models.Node.DoesNotExist:
            raise NotFound()

    def data(self):
        return {
            'name': self.model.name,
        }

    def render(name):
        data = self.data()
        for attr in self.model.nodeattribute_set.all():
            labels = attr.name.split('.')
            for label in labels:
                pass
        return data
