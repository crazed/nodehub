from django.contrib import admin
from nodehub.apps.ip import models

class Network(admin.ModelAdmin):
    fields = ('address', 'prefixlen', 'vlan', 'name')
    list_display = ('address', 'prefixlen', 'vlan')

class Address(admin.ModelAdmin):
    fields = ('address', 'prefixlen', 'name')
    list_display = ('address', 'prefixlen')

class VLAN(admin.ModelAdmin):
    fields = ('identifier', 'name')
    list_display = ('identifier', 'name')

admin.site.register(models.Network, Network)
admin.site.register(models.Address, Address)
admin.site.register(models.VLAN, VLAN)
