"""
Django settings for app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h3i_2*vn9kf(bc_0u=9z5e^24=$v9)h(_u0yx4yw3uod92_7uh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', None)
if DEBUG is not None:
    DEBUG = (DEBUG == 'True')

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testresults',
    'mptt',
    'django_extensions',
    'tokenapi',
    'bootstrap3',
    'django_rq',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'tokenapi.backends.TokenBackend',
)

# We want to use tokens as long term auth for the upload test result api
TOKEN_TIMEOUT_DAYS = 99999

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testresults',
        'USER': 'testresults',
        'PASSWORD': 'testing',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

import dj_database_url
DATABASES['default'] =  dj_database_url.config(default=DATABASES['default'])
DATABASES['default']['CONN_MAX_AGE'] = 500

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

RQ_QUEUES = {
    'default': {
        'URL': os.getenv('REDIS_URL', 'redis://localhost:6379'), # If you're on Heroku
        'DB': 0,
        'timeout': 1800,
    },
    'high': {
        'URL': os.getenv('REDIS_URL', 'redis://localhost:6379'), # If you're on Heroku
        'DB': 0,
        'timeout': 1800,
    },
    'low': {
        'URL': os.getenv('REDIS_URL', 'redis://localhost:6379'), # If you're on Heroku
        'DB': 0,
        'timeout': 1800,
    },
}
