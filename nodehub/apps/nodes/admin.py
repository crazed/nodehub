from django.contrib import admin
from nodehub.apps.nodes import models

class Interface(admin.TabularInline):
    model = models.Interface
    fields = ('name', 'links')
    extra = 0
    filter_horizontal = ('links',)

class NetworkInterface(admin.TabularInline):
    model = models.NetworkInterface
    fields = ('name', 'links', 'ip_addresses', 'mac_address')
    extra = 0
    filter_horizontal = ('links', 'ip_addresses')

class NodeModifier(admin.TabularInline):
    model = models.NodeModifier
    fields = ('name', 'operator', 'value', 'priority')
    extra = 0

class Node(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    inlines = [NetworkInterface, Interface, NodeModifier]

class GroupModifier(admin.TabularInline):
    model = models.GroupModifier
    fields = ('name', 'operator', 'value', 'priority')
    extra = 0

class Group(admin.ModelAdmin):
    fields = ('name', 'nodes')
    list_display = ('name',)
    filter_horizontal = ('nodes',)
    inlines = [GroupModifier]

admin.site.register(models.Node, Node)
admin.site.register(models.Group, Group)
