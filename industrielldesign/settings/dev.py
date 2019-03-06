from industrielldesign.settings.base import *

# Override base.py settings here

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'..', 'db.sqlite3'),
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '..', 'assets'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), '..', 'media')
