"""
Settings for local development.
Do not use these settings for production!
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from .base import * # noqa

SECRET_KEY = 'secret key for local development only!'

DEBUG = True
