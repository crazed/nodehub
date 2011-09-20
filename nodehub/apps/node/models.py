from nodehub.db import models

class Node(models.BaseModel):
    name = models.NameField(blank=False, unique=True, help_text='Use fully qualified domain name whenever possible')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Host(Node):
    pass

class NodeModifier(models.ModifierModel):
    node = models.ForeignKey(Node)

class Interface(models.BaseModel):
    node = models.ForeignKey(Node)
    name = models.CharField(max_length=32)
    links = models.ManyToManyField('self', blank=True)

    def __unicode__(self):
        return '%s :: %s' % (self.node.name, self.name)

    class Meta:
        ordering = ['name']
        unique_together = (('node', 'name'),)

class NetworkInterface(Interface):
    ip_addresses = models.ManyToManyField('ip.Address', blank=True)
    mac_address = models.MACAddressField(blank=True, null=True)

class Group(models.BaseModel):
    name = models.NameField(unique=True)
    nodes = models.ManyToManyField(Node, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class GroupModifier(models.ModifierModel):
    group = models.ForeignKey(Group)
