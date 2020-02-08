from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']


INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'olive',
        'USER': 'postgres',
        'PASSWORD': 'nollywood10',
        'HOST': '127.0.0.1',
        'PORT': 5433,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '127.0.0.1'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'vtu@mailing.vtubusinessportal.com' 

THEME_CONTACT_EMAIL = DEFAULT_FROM_EMAIL #os.getenv('THEME_CONTACT_EMAIL')
ADMINS = (('Admin', THEME_CONTACT_EMAIL),)
MANAGERS = ADMINS
EMAIL_SUBJECT_PREFIX = ''
SEND_BROKEN_LINK_EMAILS=True
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_PORT = os.getenv('EMAIL_PORT')
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
# EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL')
# SERVER_EMAIL = os.getenv('SERVER_EMAIL')
# DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
# EMAIL_HOST = os.getenv('EMAIL_HOST')
