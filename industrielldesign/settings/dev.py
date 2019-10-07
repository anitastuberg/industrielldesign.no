from industrielldesign.settings.base import *

# Override base.py settings here

DEBUG = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), '..', 'media')
EMAIL_HOST_PASSWORD = ''
