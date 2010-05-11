# Django settings for mysite project.
import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = '/home/brencam/_DjangoApps/website/webapps/webappdb.sqlite'
#DATABASE_NAME = '/home/brencam/_DjangoApps/website/webappdb.sqlite'
DATABASE_NAME = '../webappdb.sqlite'

DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
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

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0$ffqo&()k^2fib1px*ous%+e^)@q7njboz_2edrxaa-278d1y'

#  new messages middleware (Django V1.1.1)
#MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

#  new messages middleware (Django V1.1.1)
#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.messages.context_processors.messages',
#)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
     #  new messages middleware (Django V1.1.1)
    #'django.contrib.sessions.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
   # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'devserver.middleware.DevServerMiddleware',
)

ROOT_URLCONF = 'webapps.urls'

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)


def custom_show_toolbar(request):
    return True # Always show toolbar, for example purposes only.


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': True,
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    'HIDE_DJANGO_SQL': False,
    'TAG': 'body',
}

INTERNAL_IPS = ('127.0.0.1',
)

DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # Modules not enabled by default
    'devserver.modules.ajax.AjaxDumpModule',
    #'devserver.modules.profile.MemoryUseModule',
    'devserver.modules.cache.CacheSummaryModule',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

      os.path.join(os.path.dirname(__file__), 'templates'),

      '/home/brencam/_DjangoApps/website/webapps/templates',   
      '/home/brencam/_DjangoApps/website/webapps/templates/oshpdapp',
      '/home/brencam/_DjangoApps/website/webapps/templates/lgapp',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    # new messages middleware 
    #'django.contrib.messages',A
    #'debug_toolbar',
    'devserver',
    'webapps.oshpdapp',
    'webapps.lgapp',
)

LOGIN_URL = '/login/'
