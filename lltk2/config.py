# -------------------
# Configuration
# -------------------

import os
from django_micro import configure

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
DEBUG = True
SECRET_KEY = 'delphi'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

configure(locals(), django_admin=True)
