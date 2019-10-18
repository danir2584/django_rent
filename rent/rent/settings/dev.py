from .base import *
import os


DEBUG = True
ALLOWED_HOSTS = []

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'frontend', "build", "static"),)

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
