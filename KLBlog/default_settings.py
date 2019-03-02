import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '6oba9lyp#(@_9#o_rn^fzx1th5go_u++g*bt)u_mtuz1vrm$=7'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'klblog',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_ROOT = None

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = []
