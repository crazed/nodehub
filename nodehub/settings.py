import os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ENV = os.environ.get('DJANGO_ENV', 'dev')

DEBUG = os.environ.get('DJANGO_DEBUG') == 'true' or ENV == 'dev'
TEMPLATE_DEBUG = DEBUG

ADMINS = (
#    ('Admin', 'admin@example.org'),
)

MANAGERS = ADMINS

if ENV == 'dev':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '.nodehub.db',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'nodehub',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
# User-uploaded files
MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')
MEDIA_URL = '/media/'
# Static files
STATIC_ROOT = os.path.join(ROOT_PATH, 'static')
STATIC_URL = '/static/'
# Admin static content
ADMIN_MEDIA_PREFIX = '/static/admin/'
# Database fixtures
FIXTURE_DIRS = os.path.join(ROOT_PATH, 'fixtures')

STATICFILES_DIRS = (
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Secret key
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'secret')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'nodehub.urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'nodehub.apps.dns',
    'nodehub.apps.ip',
    'nodehub.apps.nodes',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
