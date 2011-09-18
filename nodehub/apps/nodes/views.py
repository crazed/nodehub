import json
from django import http
from nodehub.apps.nodes import api

def get(request, name):
    try:
        node = api.Node(name)
    except api.NotFound:
        raise http.Http404()
    return http.HttpResponse(json.dumps(node.data()))

def render(request, name):
    return get(request, name)
