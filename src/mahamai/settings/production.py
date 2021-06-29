from .base import *

DEBUG = False

ALLOWED_HOSTS = ['mahamai.ir', 'mahamai.iran.liara.run', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database' / 'db.sqlite3',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtppro.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'this_is_not_password')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

