import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'eaatdw+e9!o16&)@esloy%hr91yw!%l=v3csmd$6ayv=8x^@lx'
DEBUG = False
ALLOWED_HOSTS = ["*"]


INSTALL_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'api',
)


MIDDLEWARE_CLASSES = (

)


ROOT_URLCONF = 'api.urls'


WSGI_APPLICATION = 'api.wsgi.application'


TEMPLATES = []
DATABASES = {}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = ''
