import ipaddr
from django.core import exceptions
from django.core.exceptions import ObjectDoesNotExist
from nodehub.db import models

class Network(models.BaseModel):
    address = models.IPAddressField(unique=True)
    broadcast = models.IPAddressField(editable=False)
    prefixlen = models.IntegerField(help_text='CIDR notation')
    vlan = models.ForeignKey('VLAN', blank=True, null=True, verbose_name='VLAN')
    name = models.CharField(max_length=256, blank=True)

    def __unicode__(self):
        return '%s/%s' % (self.address, self.prefixlen)

    def clean(self, *args, **kwargs):
        try:
            network = self.ipaddr()
        except ValueError, error:
            raise exceptions.ValidationError('Invalid network.')
        if Address.objects.filter(address=self.address).exists():
            raise exceptions.ValidationError('Network address conflicts with current IP address.')
        network_list = Network.objects.all()
        network_list = network_list.filter(address__gte=self.address)
        network_list = network_list.filter(broadcast__lte=self.address)
        network_list = network_list.exclude(pk=self.id)
        for network_current in network_list:
            raise exceptions.ValidationError('Network overlaps with %s/%s.' %
                (network_current.address, network_current.subnet))
        super(Network, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.broadcast = self.ipaddr().broadcast
        super(Network, self).save(*args, **kwargs)

    def ipaddr(self):
        return ipaddr.IPNetwork('%s/%s' % (self.address, self.prefixlen), strict=True)

    class Meta:
        ordering = ['address', 'prefixlen']
        unique_together = (('address', 'prefixlen'),)

class Address(models.BaseModel):
    address = models.IPAddressField()
    prefixlen = models.IntegerField(help_text='CIDR notation', blank=True, null=True)
    name = models.CharField(max_length=256, blank=True)

    def __unicode__(self):
        return unicode(self.address)

    def clean(self):
        try:
            ip = self.ipaddr()
        except ValueError, error:
            raise exceptions.ValidationError('Invalid IP address.')

    def save(self, *args, **kwargs):
        if not self.prefixlen:
            try:
                network = Network.objects.filter(address__lt=self.address, broadcast__gt=self.address)
                network = network.get()
                if network:
                    self.prefixlen = network.prefixlen
            except ObjectDoesNotExist:
                pass
        super(Address, self).save(*args, **kwargs)

    def ipaddr(self):
        return ipaddr.IPAddress(self.address)

    class Meta:
        ordering = ['address', 'prefixlen']
        unique_together = (('address', 'prefixlen'),)

class VLAN(models.BaseModel):
    identifier = models.PositiveIntegerField(unique=True, verbose_name='ID')
    name = models.CharField(max_length=256, blank=True)

    def __unicode__(self):
        return unicode(self.identifier)

    class Meta:
        verbose_name = 'VLAN'
        ordering = ['identifier']
