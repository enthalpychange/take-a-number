"""
Settings for local development.
Do not use these settings for production!
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from .base import * # noqa

SECRET_KEY = 'secret key for local development only!'

DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
#
# docker run -d -e "POSTGRES_PASSWORD=postgres" -p 127.0.0.1:5432:5432 postgres

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'PORT': '',
    }
}

LOCAL_APPS = [
    'debug_toolbar',
]

INSTALLED_APPS += LOCAL_APPS # noqa

LOCAL_MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

MIDDLEWARE += LOCAL_MIDDLEWARE # noqa

# 127.0.0.1 required for debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

DEBUG_TOOLBAR_CONFIG = {
    # Redirects Panel is disabled by default
    # Uncomment to enable Redirects Panel
    # 'DISABLE_PANELS': {},
}
