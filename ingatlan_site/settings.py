import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 SECURITY
SECRET_KEY = 'django-insecure-CHANGE_ME'
DEBUG = True

ALLOWED_HOSTS = ['*']


# =========================
# 🔥 RENDER FIX (LOGIN / COOKIE)
# =========================
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_TRUSTED_ORIGINS = [
    "https://ingatlan-app.onrender.com",
]

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'

SESSION_ENGINE = 'django.contrib.sessions.backends.db'


# =========================
# 🔌 APPS
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'listings',
]


# =========================
# 🧱 MIDDLEWARE
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =========================
# 🔗 URL
# =========================
ROOT_URLCONF = 'ingatlan_site.urls'


# =========================
# 🎨 TEMPLATES
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # fontos!
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =========================
# ⚙️ WSGI
# =========================
WSGI_APPLICATION = 'ingatlan_site.wsgi.application'


# =========================
# 🗄 DATABASE
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================
# 🔑 PASSWORD
# =========================
AUTH_PASSWORD_VALIDATORS = []


# =========================
# 🌍 LANG
# =========================
LANGUAGE_CODE = 'hu'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True


# =========================
# 📁 STATIC
# =========================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# =========================
# 🔐 LOGIN FIX
# =========================
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'
LOGOUT_REDIRECT_URL = '/accounts/login/'


# =========================
# 🔥 CLOUDINARY (ENV-ből!)
# =========================
import cloudinary

cloudinary.config(
    secure=True
)

# FONTOS:
# Render-en legyen beállítva:
# CLOUDINARY_URL = cloudinary://API_KEY:API_SECRET@CLOUD_NAME


# =========================
# DEFAULT
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'