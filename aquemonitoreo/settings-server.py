"""
Django settings for aquemonitoreo project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = "/home/Aquemonitoreo/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+0s_7p5=1l*il)-_x0m&mmzb4)k2074n-1kye)pd4@ly3$(@o+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["monitoreo.aquieneselegimos.org.py","aquieneselegimos.org.py","45.55.93.88","127.0.0.1"]

APPEND_SLASH=True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'tinymce', # Texto enriquecido
    'ckeditor',
    'ckeditor_uploader',
    'main',
    'constance'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aquemonitoreo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/main/templates',

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

WSGI_APPLICATION = 'aquemonitoreo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
     'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'hola09',
        'HOST': 'localhost',
        'PORT': '5432',
	}
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


STATIC_ROOT = BASE_DIR + '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "main/static"),
    
]

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

CKEDITOR_UPLOAD_PATH = "uploads/"


CONSTANCE_BACKEND =  'constance.backends.database.DatabaseBackend'

from ckeditor.widgets import CKEditorWidget

CONSTANCE_ADDITIONAL_FIELDS = {
    'ckeditor': ['django.forms.fields.CharField', {
        'widget': 'ckeditor.widgets.CKEditorWidget',
     
    }],
}


CONSTANCE_CONFIG = {
    'QUIENES_SOMOS_PORTADA': ('', 'Lo que va en la seccion de Quienes somos de la Portada', 'ckeditor'),
    'QUIEN_NOS_AYUDA': ('', 'Seccion de Quien mas nos ayuda de la Portada', 'ckeditor'),
    'QUIENES_SOMOS': ('', 'Lo que va en la seccion de Quienes somos', 'ckeditor'),
    'METODOLOGIA': ('', 'Contenido de la paginas Metodologia', 'ckeditor'),
    'ACERCA_DE': ('', 'Acerca del Proyecto', 'ckeditor'),
    
}

CONSTANCE_CONFIG_FIELDSETS = {
'PORTADA': ('QUIENES_SOMOS_PORTADA','QUIEN_NOS_AYUDA'),
'General Options': ('QUIENES_SOMOS', 'METODOLOGIA','ACERCA_DE'),
    
}

