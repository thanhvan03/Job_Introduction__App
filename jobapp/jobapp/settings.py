"""
Django settings for jobapp project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(el(5*4st279!3kq(kf84@f!-_j#^-pf=crh1b76q&bb%nq7y&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobs.apps.JobsConfig',
    'ckeditor',
    'ckeditor_uploader',
    'debug_toolbar',
    'rest_framework',
    'drf_yasg',
    'cloudinary',
    'oauth2_provider',
    'django_extensions',
]

import pymysql

pymysql.install_as_MySQLdb()

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'jobapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'jobapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jobapp',
        'USER': 'root',
        'PASSWORD': 'Thv@n003',
        'HOST': ''
    }
}

AUTH_USER_MODEL = 'jobs.User'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_ROOT = '%s/jobs/static/images' % BASE_DIR
CKEDITOR_UPLOAD_PATH = "ckeditor/images/"

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

import cloudinary

cloudinary.config(
    cloud_name="daiq8cr59",
    api_key="526432242612972",
    api_secret="xFbKXPf-oTOrXWmIq__14XZYWAI"
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    )
}

# CLIENT_ID1 = 'fsUK8nC7BLEPvoRV2jCHj9mEvaTUK7px2bfsZko5'
# CLIENT_SECRET1 = 'pFYeaKEYExdRd37ojHYDKUNEJTfMHQZFaZGJSLAOsAKbtCH9NGcITSq2XPTl3OG7p2tQkk81wU70JdQPbF4rBEzIVGnzH32nZMW9uPDQ4X6XPUhzYRGU87tWl2A2pS1I'

CLIENT_ID = 'AaHYNz98r6Wt1CTb0DH08lOH9aRNLObpdXrfZct2'
CLIENT_SECRET = '42mZx2dWb3ns6YO1KvEJ8ugPgErNwmjI1zmaRnnw74llMwzyUdogr4tdb9M9gvqady2Zyym48bzUvh4ic6VGQKascwbQRMTqRoYvgOyN0dQZ2nfuuV05zhWA46K3VZeA'

#OAUTH2_PROVIDER = {'OAUTH2_provider.oauth2_backends.JSONAuthLibCore'}

