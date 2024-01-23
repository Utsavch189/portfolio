"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import datetime
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%x@46uo!r9#x4s0!@&c9yc)q1s5o1=ws13p07h1&o*c@f98(hg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dbbackup',
    'django_crontab',
    'rest_framework',
    'corsheaders',
    'src.mail.apps.MailConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'db_backup'}

CRONJOBS = [
    ('0 6 * * *','core.cronjob.db_backUp')
]

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xvqwtkcw_utsavdb',
        'USER': 'xvqwtkcw_utsav',
        'PASSWORD': 'utsav@2001',
        'HOST':'65.109.122.227',
        'PORT':3306,
         "OPTIONS": {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
            'charset': 'utf8mb4',
            "autocommit": True,
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_HOST = 'server5.dnspark.in'
EMAIL_PORT = 465
EMAIL_HOST_USER='officail@utsavchatterjee.me'
EMAIL_HOST_PASSWORD= 'utsav@2001'

CELERY_BROKER_URL='redis://default:Hb5l2ZpMFAEKug22yzIEvo12KxVpSqTF@redis-16032.c274.us-east-1-3.ec2.cloud.redislabs.com:16032'
CELERY_ACCEPT_CONTENT=['application/json']
CELERY_TASK_SERIALIZER='json'
CELERY_TIMEZONE='Asia/Kolkata'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ORIGIN_ALLOW_ALL=False
APPEND_SLASH=True

LOGGING ={
    'version':1,
    "disable_existing_loggers": False,
    'loggers':{
        'success':{
            'handlers':['success_file'],
            'level':'INFO'
        },
        'error':{
            'handlers':['error_file'],
            'level':'ERROR'
        }
    },
    'handlers':{
        'success_file':{
            'class': 'logging.FileHandler',
            'filename':'./logs/success/'+str(datetime.date.today())+'.log',
            'formatter':'simpleRe',
        },
        'error_file':{
            'class': 'logging.FileHandler',
            'filename':'./logs/error/'+str(datetime.date.today())+'.log',
            'formatter':'simpleRe',
        }
    },
    'formatters':{
        'simpleRe': {
            'format': '{levelname} : [{asctime} {lineno:d} {process:d} {thread:d} {message}]',
            'datefmt' : "%d/%b/%Y %H:%M:%S",
            'style': '{',
        }

    }
}