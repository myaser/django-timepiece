import sys
import dj_database_url

from .base import *  # noqa

DATABASES['default'] = dj_database_url.config()
ALLOWED_HOSTS += ['timepiece-demo.herokuapp.com']
ROOT_URLCONF = 'example_project.urls'
DEBUG = os.environ.get('DJANGO_DEBUG', 'False')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    }
}

ADMINS=[('mahmoud yaser', 'm.yaser@cubeegypt.com')]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'