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

class NodeAttribute(admin.TabularInline):
    model = models.NodeAttribute
    fields = ('name', 'modifier', 'value', 'priority')
    extra = 0

class Node(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    inlines = [NetworkInterface, Interface, NodeAttribute]

class GroupAttribute(admin.TabularInline):
    model = models.GroupAttribute
    fields = ('name', 'modifier', 'value', 'priority')
    extra = 0

class Group(admin.ModelAdmin):
    fields = ('name', 'nodes')
    list_display = ('name',)

admin.site.register(models.Node, Node)
admin.site.register(models.Group, Group)
