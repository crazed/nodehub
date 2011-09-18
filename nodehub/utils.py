import re
import string
from django.core import exceptions

# This should probably be more liberal
DNS_LABEL_TEXT = '(?![-\d])[a-zA-Z0-9-_]{1,63}(?<!-)'
DNS_LABEL_RE = re.compile('^%s$' % DNS_LABEL_TEXT)

HOST_LABEL_TEXT = '(?![-\d])[a-zA-Z0-9-]{1,63}(?<!-)'
HOST_LABEL_RE = re.compile('^%s$' % HOST_LABEL_TEXT)

def validate_dns_name(value, hostname=True, error_text=''):
    if hostname:
        if not all(HOST_LABEL_RE.match(x) for x in value.split('.')):
            raise exceptions.ValidationError(error_text or 'Enter a valid hostname.')
    else:
        if not all(DNS_LABEL_RE.match(x) for x in value.split('.')):
            raise exceptions.ValidationError(error_text or 'Enter a valid DNS name.')

def validate_mac_address(value):
    before_length = len(value)
    value = ''.join([c for c in value if c in string.hexdigits])
    after_length = len(value)

    if before_length != after_length or after_length != 12:
        exceptions.ValidationError('Enter a valid MAC address.')

    return value
