
import os

DEBUG = True


# Django 1.2 up
DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'test.db')

# Django 1.1 and 1.0
DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'NAME': DATABASE_NAME
    }
}

ROOT_URLCONF = 'testproject.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes', # Required for auth
    'django.contrib.admin',        # Required by django.contrib.auth tests
    'django.contrib.sites',        # Required by django.contrib.auth tests 
    
    'urldecorators',               # Optional, only for Django test runner 
)

SITE_ID = 1

LOGIN_URL = '/login/'
