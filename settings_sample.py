#
# Django settings for MaizeDIG: Maize Database for Images ange Gnomes
# Django version: 1.3.7
#
# Updated by Kyoung Tak Cho
#

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Kyoung Tak Cho', 'ktcho'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DB_NAME_HERE',
        'USER': 'USERNAME_HERE',
        'PASSWORD': 'PASSWORD_HERE',
        'HOST': 'localhost',
        'PORT': '',
    },
    'mgdb': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=mgdb'
        },
        'NAME': 'DB_NAME_HERE',
        'USER': 'USERNAME_HERE',
        'PASSWORD': 'PASSWORD_HERE',
        'HOST': 'mgdb-curation.usda.iastate.edu',
        'PORT': '5432',
    },
    'mgdb2': {
        'ENGINE': 'django.db.backends.oracle',
        'OPTIONS': {
            'options': '-c search_path=mgdb'
        },
        'NAME': 'DB_NAME_HERE',
        'USER': 'USERNAME_HERE',
        'PASSWORD': 'PASSWORD_HERE',
        'HOST': 'planter2.usda.iastate.edu',
        'PORT': '1521',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# THE ALIAS FOR THE WEBSITE
# (change depending on devo server/gamma/prod)
SITE_URL = '/'

# Set current working directory
cur_path = os.path.dirname(os.path.realpath(__file__))
projectName = cur_path.split(os.sep)[-1]
mainAppName = "taxon_home"

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(cur_path, mainAppName, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = SITE_URL + 'media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(cur_path, "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = SITE_URL + 'static_site/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = SITE_URL + 'static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(cur_path, mainAppName, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Directory inside the template directoryfor the pagelets to be found
PAGELET_LAYOUT_DIR = 'pageletLayouts/'

#Directory inside template directory for the application layouts to be found
APPLICATION_LAYOUT_DIR = 'applicationLayouts/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'MAKE A UNIQUE KEY HERE'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

#ROOT_URLCONF = 'MaizeDIG.urls'
ROOT_URLCONF = projectName + '.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(cur_path, mainAppName, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    mainAppName
)

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s $(message)s'
        },
    },
    'handlers': {
        'file':{
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(cur_path, "logs", "debug.log"),
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'MaizeDIG': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

DATABASE_ROUTERS = [mainAppName + '.routers.DBRouter']


# Constants for setting up rate limiting on web services
# Note: This will rate limit all programs but will not 
# effect the pages viewable to the public as those pages 
# only use the web services internally
RATE_LIMIT = False # Set to false to disable rate limiting
TIMEOUT = 1 # number of minutes before cache timeout
MAX_REQUESTS = 100 # number of request allowed before cache timeout

#
# Feedback
#
FEEDBACK_EMAIL = 'totaks@gmail.com'

