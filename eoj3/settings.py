"""
Django settings for eoj3 project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

def get_secret_key():
    try:
        from .local_settings import SECRET_KEY
        return SECRET_KEY
    except ImportError:
        return 'd#w%dw^4lzdqn8g*2=r^yg3b3#qgq$g8%ipa+4xnjutj39_xi='

SECRET_KEY = get_secret_key()

def get_debug_option():
    try:
        from .local_settings import DEBUG
        return DEBUG
    except ImportError:
        return True

DEBUG = get_debug_option()

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'django.contrib.staticfiles',
    'django.contrib.humanize',

    'home',
    'account',
    'dispatcher',
    'problem',
    'backstage',
    'submission',
    'contest',
    'utils',
    'tests',
    'blog',

    # third-party packages
    'widget_tweaks',
    'django_jinja',
    'tagging',
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

ROOT_URLCONF = 'eoj3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'OPTIONS': {'environment': 'eoj3.jinja2.environment'},
        'APP_DIRS': True,
        'OPTIONS': {
            "undefined": None,
            "match_extension": ".jinja2",
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            "globals": {
                "myGlobal": "utils.jinja2.globals.is_active",
                "myGlobal2": "utils.jinja2.globals.paginator",
                "myGlobal3": "utils.jinja2.globals.render_field",
                "myGlobal4": "utils.jinja2.globals.url_replace",
                "myGloabl5": "utils.jinja2.globals.static_file_modify",
            },
            "filters": {
                "myFilter": "utils.jinja2.filters.status_choice",
                "myFilter2": "utils.jinja2.filters.timedelta_format",
                "myFilter3": "utils.jinja2.filters.markdown_format",
                "myFilter4": "utils.jinja2.filters.sample_format",
                "myFilter5": "utils.jinja2.filters.minute_format",
                "myFilter6": "utils.jinja2.filters.get_intro",
            },
            "tests": {
                "myTest": "utils.jinja2.tests.is_admin",
            }
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'eoj3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

def get_database():
    try:
        from .local_settings import DATABASES
        return DATABASES
    except ImportError:
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                'OPTIONS': {
                    'timeout': 15000,
                }
            }
        }

DATABASES = get_database()

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    }
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_DIR = os.path.join(BASE_DIR, 'static')

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# my settings
AUTH_USER_MODEL = 'account.User'
SESSION_COOKIE_AGE = 1209600  # default 2 weeks
LOGIN_URL = '/login/'
TESTDATA_DIR = os.path.join(BASE_DIR, "data")
UPLOAD_DIR = os.path.join(BASE_DIR, "upload")
GENERATE_DIR = os.path.join(BASE_DIR, "generate")
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
DATETIME_FORMAT = 'Y-m-d H:i'  # only for django templates

# modified
TIME_ZONE = 'Asia/Shanghai'
# TIME_ZONE = 'UTC'
USE_L10N = False
USE_TZ = False


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'utils.authentication.UnsafeSessionAuthentication',
    )
}