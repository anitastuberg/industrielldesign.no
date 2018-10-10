from industrielldesign.settings.base import *

# Override base.py settings here
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LeonardoLinjefor$industrielldesign',
        'USER': 'LeonardoLinjefor',
        'PASSWORD': config.DATABASE_PASSWORD,
        'HOST': 'LeonardoLinjeforening.mysql.pythonanywhere-services.com'
    }
}

# HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True