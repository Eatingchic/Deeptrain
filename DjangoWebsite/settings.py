"""
Django settings for DjangoWebsite project.

Generated by 'django-admin startproject' using Django 3.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#l#3ps7+(*+7f#0cz=aj-sp!6$-waaf6h=*+=5h*(5njj_^)@8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition
APPLICATIONS_CONFIG_FILE = "config.json"
BASE_APPLICATION_DIR = os.path.join(BASE_DIR, "applications")
APPLICATIONS_DIR = [f"applications.{app_path}" for app_path in os.listdir(BASE_APPLICATION_DIR)
                    if os.path.isdir(os.path.join(BASE_APPLICATION_DIR, app_path)) and app_path != "__pycache__"
                    and os.path.isfile(os.path.join(BASE_APPLICATION_DIR, app_path, APPLICATIONS_CONFIG_FILE))]

# Captcha  /captcha/conf/settings
CAPTCHA_IMAGE_SIZE = (80, 30)
CAPTCHA_LENGTH = 4
CAPTCHA_TIMEOUT = 1  # minutes
CAPTCHA_FONT_SIZE = 20
CAPTCHA_OUTPUT_FORMAT = '%(text_field)s %(image)s %(hidden_field)s'
CAPTCHA_NOISE_FUNCTIONS = (
   'captcha.helpers.noise_null',
   'captcha.helpers.noise_arcs',
   'captcha.helpers.noise_dots',
)
# 随机字符验证码
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dwebsocket',
    'captcha',
    'model',
    'IMServer',
    'fileHandler',
] + APPLICATIONS_DIR

#  appHandler.app_settings(): django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.CodecMiddleware.CodecMiddleware'
    # 'dwebsocket.middleware.WebSocketMiddleware',
]

ROOT_URLCONF = 'DjangoWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'django.templatetags.static'
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoWebsite.wsgi.application'
# WEBSOCKET_FACTORY_CLASS = 'dwebsocket.backends.uwsgi.factory.uWsgiWebSocketFactory'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.mysql',  # module
            'NAME': 'django-database',  # database name
            'HOST': 'localhost',  # ip
            'PORT': 3306,
            'USER': 'root',
            'PASSWORD': 'zmh200904',
        }
}

# Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Encode / Decode
CODING = "utf-8"
WS_INTERVAL = 0.04
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "/static/")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
