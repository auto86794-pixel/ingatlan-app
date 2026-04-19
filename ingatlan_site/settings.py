import os
from pathlib import Path
import cloudinary

# BASE
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = 'django-insecure-CHANGE_THIS'

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'ingatlan-app.onrender.com',
]

# INSTALLED APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'listings',
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL
ROOT_URLCONF = 'ingatlan_site.urls'

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # fontos!
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

# WSGI
WSGI_APPLICATION = 'ingatlan_site.wsgi.application'

# DATABASE (SQLite egyszerűség kedvéért)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = []

# LANGUAGE
LANGUAGE_CODE = 'hu'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

# STATIC
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# LOGIN
LOGIN_REDIRECT_URL = '/create/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# =========================
# 🔥 CLOUDINARY FIX
# =========================

cloudinary.config(
    cloud_name="drdvqyl4b",
    api_key="652588949169875",
    api_secret="UXWfHKmSH26UKtkzhBLL_ikzWlM"  # <-- IDE A TE SECRETED
)

# DEFAULT
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'