import dj_database_url
import psycopg2

from industrielldesign.settings.base import *

# Override base.py settings here
DEBUG = True

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = 'DENY'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
