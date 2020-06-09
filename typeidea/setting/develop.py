from .base import *  #NOQA


DEBUG = True

DATABASES = {
    'default': {
        'ENIGNE': 'django.db.backends.sqlites',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite'),
    }
}