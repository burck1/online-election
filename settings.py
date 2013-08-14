DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Alex Burck', 'alex@theburcks.com'),
    ('Jacob Fuss', 'jacobfuss4@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'onlineelection',
        'USER': 'strax',
        'PASSWORD': 'tardis',
        'HOST': 'mysql.theburcks.com',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = '/home/strax/theburcks.com/public/media'
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'l!6vc-g+u!fal=+=a(q#=!0qf3gk8ycye256fzmxw9+6+yj0q4'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'OnlineElection.urls'

TEMPLATE_DIRS = (
    "/home/strax/theburcks.com/OnlineElection/templates",
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # User Apps
    'polls'
)
