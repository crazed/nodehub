from django.shortcuts import render_to_response, get_object_or_404
from nodehub.apps.nodes import models

def node_detail(request, name):
    n = get_object_or_404(models.Node, name=name)
    return render_to_response('nodes/node_detail.html', {'node': n})
