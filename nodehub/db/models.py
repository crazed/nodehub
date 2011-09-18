import decimal
import ipaddr
from django.contrib.auth import models as auth_models
from django.core import exceptions
from django.db.models import *
from nodehub import forms
from nodehub import utils

class IPAddressField(Field):
    __metaclass__ = SubfieldBase
    description = 'An IP address stored as a decimal'

    def _format(self, value):
        try:
            return unicode(self.to_python(value)) or ''
        except ValueError:
            return ''

    def clean(self, value, *args, **kwargs):
        value = super(IPAddressField, self).clean(value, *args, **kwargs)
        try:
            self.to_python(value)
        except ValueError:
            raise exceptions.ValidationError('Enter a valid IP address.')
        return value

    def to_python(self, value):
        if not value:
            return None

        if isinstance(value, (ipaddr.IPv4Network, ipaddr.IPv6Network)):
            return value.network
        elif isinstance(value, (ipaddr.IPv4Address, ipaddr.IPv6Address)):
            return value
        elif isinstance(value, decimal.Decimal):
            value = int(value)

        return ipaddr.IPAddress(value)

    def get_internal_type(self):
        return 'DecimalField'

    def get_db_prep_value(self, value, connection, prepared=False):
        return connection.ops.value_to_db_decimal(
            decimal.Decimal(int(self.get_prep_value(value))),
            39, 0)

    def get_prep_value(self, value):
        return self.to_python(value)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.IPAddressField}
        defaults.update(kwargs)
        return super(IPAddressField, self).formfield(**defaults)

class MACAddressField(fields.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 12
        super(MACAddressField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.MACAddressField}
        defaults.update(kwargs)
        return super(MACAddressField, self).formfield(**defaults)

class NameField(fields.CharField):

    def __init__(self, hostname=True, *args, **kwargs):
        kwargs['max_length'] = 255
        self.hostname = hostname
        super(NameField, self).__init__(*args, **kwargs)

    def clean(self, value, *args, **kwargs):
        value = super(NameField, self).clean(value, *args, **kwargs)
        if value:
            utils.validate_dns_name(value, self.hostname)
        return value

class TimestampModel(Model):
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseModel(TimestampModel):

    class Meta:
        abstract = True

class AttributeModel(BaseModel):
    MOD_CHOICES = (
        (1, 'set'),
        (2, 'unset'),
    )
    name = CharField(max_length=255)
    modifier = IntegerField(choices=MOD_CHOICES)
    value = TextField(blank=True)
    priority = IntegerField(default=0)

    def __unicode__(self):
        return u'%s %s %s' % (self.name, self.modifier, self.value)

    class Meta:
        abstract = True
        ordering = ['name', 'priority']
