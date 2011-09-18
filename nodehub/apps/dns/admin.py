from django.contrib import admin
from nodehub.apps.dns import models

class Record(admin.TabularInline):
    model = models.Record
    fields = ('name', 'type', 'content', 'priority', 'ttl')
    extra = 0

class Zone(admin.ModelAdmin):
    fields = ('name', 'ttl')
    inlines = [Record]
    list_display = ('name', 'ttl')
    search_fields = ('name',)

admin.site.register(models.Zone, Zone)
