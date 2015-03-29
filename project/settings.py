# -*- coding: utf-8 -*-

DEFAULT_TIMEZONE = 'UTC'
DEBUG = True
PROFILE = False
SECRET_KEY = 'ReplaceItWithSecretString'
SESSION_PREFIX = 'gaesess:'
COOKIE_AGE = 1209600
COOKIE_NAME = 'KAY_SESSION'

ADMINS = (
)

TEMPLATE_DIRS = (
)

USE_I18N = False
DEFAULT_LANG = 'en'

INSTALLED_APPS = (
    'core',
    'main',
    'admin',
)

APP_MOUNT_POINTS = {
    'main': '/',
    'admin': '/admin',
}

# You can remove following settings if unnecessary.
CONTEXT_PROCESSORS = (
    'kay.context_processors.request',
    'kay.context_processors.url_functions',
    'kay.context_processors.media_url',
)

MIDDLEWARE_CLASSES = (
    'kay.utils.flash.FlashMiddleware',
)
