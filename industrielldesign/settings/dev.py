from industrielldesign.settings import config
from industrielldesign.settings.base import *

# Override base.py settings here

DEBUG = True

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '..', 'assets'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), '..', 'media')
EMAIL_HOST_PASSWORD = config.EMAIL_PASSWORD