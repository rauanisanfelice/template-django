import os
import logging.config

from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
STAGE = config('STAGE', default='prod', cast=str)

ADMINS = [
    ('Nome', 'Email'),
]
if STAGE=='prod':
    ADMINS += [('Nome', 'Email'),]

MANAGERS = ADMINS

ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1']

INTERNAL_IPS = [
    'localhost',
    '127.0.0.1',
]

CORS_ORIGIN_ALLOW_ALL = DEBUG

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'example',
    'bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASS'),
        'TEST': {
            'NAME': 'defaulttests',
        }
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#############################################################
# STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    './static/',
]


#############################################################
# LOGIN / LOGOUT
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/accounts/login/'


#############################################################
# SESSION
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


#############################################################
# E-MAIL OPTIONS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = config('DJANGO_EMAIL_TLS', cast=bool)
EMAIL_HOST = config('DJANGO_EMAIL_HOST')
EMAIL_PORT = config('DJANGO_EMAIL_PORT')

EMAIL_HOST_USER = config('DJANGO_EMAIL_USER')
EMAIL_HOST_PASSWORD = config('DJANGO_EMAIL_PASSWORD')

EMAIL_FROM = config('DJANGO_EMAIL_USER')
DEFAULT_FROM_EMAIL = config('DJANGO_EMAIL_USER')


#############################################################
# CONFIGURAÇÕES AWS S3
# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_STORAGE_BUCKET_NAME = ''
# AWS_S3_REGION_NAME = ''
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_FILE_OVERWRITE = False


#############################################################
# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(name)s %(filename)s:%(lineno)s %(funcName)s %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'file': {
            'format': '%(asctime)s %(name)s %(filename)s:%(lineno)s %(funcName)s %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'console',
            'level': 'INFO',
        },
        'file': {
            'level': config('LOGLEVEL'),
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR+'/logs/debug.log',
            'formatter': 'file',
            'maxBytes': 10 * 1024 * 1024, # 10MB
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'console',
            'filters': ['require_debug_false'],
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console', 'file'],
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
        },
        'django.db.backends': {
            'level': 'DEBUG',
        },
    },
}