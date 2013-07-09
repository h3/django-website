# -*- coding: utf-8 -*-

from {{ project_name }}.conf.settings.dev import *

DEV_SERVER = False
DEBUG_TOOLBAR = False

DISABLED_APPS = ['sentry']

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'ENGINE': 'django.db.backends.mysql',
        #'ENGINE': 'django.db.backends.oracle',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    }
}

if DEV_SERVER:
    INSTALLED_APPS = INSTALLED_APPS + ('devserver',)
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('devserver.middleware.DevServerMiddleware',)


if DEBUG_TOOLBAR:
    INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', 'dev')
    INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
