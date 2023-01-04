import django_on_heroku
from decouple import config

from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG')

ALLOWED_HOSTS = [
    'web-production-5ee9.up.railway.app/',
    'pasoanchova.com'
]

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGIN = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'verbose':{
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineon)s] %(messages)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple':{
            'format':"%(levelname)s %(messages)s"
        },
    },
    'handlers':{
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers':{
        'MYAPP':{
            'handlers': ["console"],
            'level': 'DEBUG'
        },
    }
}

CSRF_TRUSTED_ORIGINS = ['https://*.pasoanchova.com']

#Heroku Settings
django_on_heroku.settings(locals())
