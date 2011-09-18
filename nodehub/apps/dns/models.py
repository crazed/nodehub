from nodehub.db import models

class Zone(models.BaseModel):
    name = models.NameField(blank=False, unique=True)
    ttl = models.IntegerField(default=86400, verbose_name='TTL', help_text='seconds')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Zone'
        ordering = ['name']

class Record(models.BaseModel):
    TYPE_CHOICES = (
        (1, 'A'),
        (2, 'NS'),
        (5, 'CNAME'),
        (12, 'PTR'),
        (15, 'MX'),
        (28, 'AAAA'),
        (33, 'SRV'),
    )
    zone = models.ForeignKey(Zone)
    name = models.NameField(blank=False, hostname=False)
    type = models.IntegerField(choices=TYPE_CHOICES)
    content = models.CharField(max_length=255)
    priority = models.IntegerField(default=0)
    ttl = models.IntegerField(default=86400, verbose_name='TTL', help_text='seconds')

    def __unicode__(self):
        return '%s.%s' % (self.name, self.zone)

    @property
    def type_name(self):
        return dict(self.TYPE_CHOICES).get(self.type, '')

    class Meta:
        verbose_name = 'Record'
        ordering = ['zone', 'name']
