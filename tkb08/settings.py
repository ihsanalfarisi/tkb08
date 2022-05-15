"""
Django settings for tkb08 project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

import dj_database_url
import os

DATABASE_URL = 'postgres://wfyawspztkvphe:4868f8dff88dbf0ca5a4b8f4d29800d8a6086d5c91f464eff907022b1d5aba4d@ec2-3-229-11-55.compute-1.amazonaws.com:5432/d37plio4p6b2p3'
 
DATABASES = {
    'default': dj_database_url.config(),
}
DATABASES['default'] = dj_database_url.config()
DATABASES['default'] = dj_database_url.config(default=DATABASE_URL)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PRODUCTION = os.environ.get('DATABASE_URL') != None


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a2x5572)z81@l+c92txcim$jde7$k5%53-pirgn7-5gxyw9p^('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'home',
    'paket_koin',

    ##oren
    'aset',
    'koleksi_aset',
    'transaksi_pembelian_aset'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'tkb08.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'tkb08.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

### ADD THIS ###
DATABASE_URL = 'postgres://wfyawspztkvphe:4868f8dff88dbf0ca5a4b8f4d29800d8a6086d5c91f464eff907022b1d5aba4d@ec2-3-229-11-55.compute-1.amazonaws.com:5432/d37plio4p6b2p3'

### CHANGE THIS ###
DATABASES = {
    'default': dj_database_url.config(),
}

### ADD THIS ###
DATABASES['default'] = dj_database_url.config()
DATABASES['default'] = dj_database_url.config(default=DATABASE_URL)

if PRODUCTION:
    DATABASES['default'] = dj_database_url.config()



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# This is the directory for storing `collectstatic` results.
# This shouldn't be included in your Git repository.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# You can use this directory to store project-wide static files.
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Add this line
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
