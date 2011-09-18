import ipaddr
from django.db import models
from django.forms import fields
from nodehub import utils

class IPAddressField(fields.CharField):

    def to_python(self, value):
        value = super(IPAddressField, self).to_python(value)
        if value in fields.validators.EMPTY_VALUES:
            return
        try:
            value = ipaddr.IPAddress(value)
        except (ValueError, TypeError):
            raise fields.ValidationError(self.error_messages['invalid'])
        return value

class MACAddressField(fields.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super(MACAddressField, self).__init__(*args, **kwargs)

    def clean(self, value, *args, **kwargs):
        super(MACAddressField, self).clean(value, *args, **kwargs)
        if value:
            value = utils.validate_mac_address(value)
        return value

    def prepare_value(self, value):
        if value:
            value = ':'.join([str(value[i:i+2]) for i in range(0, len(value), 2)])
        return super(MACAddressField, self).prepare_value(value)

class HostnameField(fields.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255
        self.error_text = kwargs.pop('error_text') if 'error_text' in kwargs else ''
        super(HostnameField, self).__init__(*args, **kwargs)

    def clean(self, value, *args, **kwargs):
        super(HostnameField, self).clean(value, *args, **kwargs)
        if value:
            utils.validate_dns_name(value, hostname=True, error_text=self.error_text)
        return value

class HostnameLikeField(HostnameField):

    def __init__(self, *args, **kwargs):
        kwargs['error_text'] = 'Valid characters are a-z, 0-9, "." and "-".'
        super(HostnameLikeField, self).__init__(*args, **kwargs)
