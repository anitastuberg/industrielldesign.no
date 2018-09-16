from industrielldesign.settings.base import *

# Override base.py settings here
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LeonardoLinjefor$industrielldesign',
        'USER': 'LeonardoLinjefor',
        'PASSWORD': 'daVincisDatabase768',
        'HOST': 'LeonardoLinjeforening.mysql.pythonanywhere-services.com',
    }
}