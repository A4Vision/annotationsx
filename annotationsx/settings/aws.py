"""
Django settings for annotationsx project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.contrib import messages
from secure import SECURE_SETTINGS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eyc+bftd*fskn^_vt4+pr)0-ih+7sc%8i40*c=cji6*#+&2paj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_extensions',
    'django_jenkins',
    'bootstrap3',
    'crispy_forms',
    'ims_lti_py',
    'hx_lti_initializer',
    'hx_lti_assignment',
    'target_object_database',
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

ROOT_URLCONF = 'annotationsx.urls'

WSGI_APPLICATION = 'annotationsx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'django_db',
# 	'USER': 'root',
# 	'PASSWORD': 'bu5egkeShy7Gphqf',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SECURE_SETTINGS.get('db_default_name', 'dce_course_info'),
            #'postgres' is in the TLT aws wiki, but won't this give access to all databases?
        'USER': SECURE_SETTINGS.get('db_default_user', 'postgres'),
        'PASSWORD': SECURE_SETTINGS.get('db_default_password'),
        'HOST': SECURE_SETTINGS.get('db_default_host', '127.0.0.1'),
        'PORT': SECURE_SETTINGS.get('db_default_port', 5432),
    } 
}


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
STATIC_ROOT = '/var/www/html'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

MESSAGE_TAGS = {
            messages.SUCCESS: 'success success',
            messages.WARNING: 'warning warning',
            messages.ERROR: 'danger error'
}

PROJECT_APPS = (
    'hx_lti_initializer',
)

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pylint',
)

CRISPY_TEMPLATE_PACK = "bootstrap3"