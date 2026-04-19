from pathlib import Path
import os
import cloudinary

# 🔐 BASE
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-CHANGE-THIS'

DEBUG = True

# ✅ RENDER FIX
ALLOWED_HOSTS = ['ingatlan-app.onrender.com', 'localhost', '127.0.0.1']


# 🔹 APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 👉 SAJÁT APP
    'listings',

    # ☁️ CLOUDINARY
    'cloudinary',
    'cloudinary_storage',
]


# 🔹 MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# 🔹 URLS
ROOT_URLCONF = 'ingatlan_site.urls'


# 🔹 TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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


# 🔹 WSGI
WSGI_APPLICATION = 'ingatlan_site.wsgi.application'


# 🔹 DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 🔹 PASSWORD
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# 🔹 LANGUAGE
LANGUAGE_CODE = 'hu-hu'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# 🔹 STATIC
STATIC_URL = 'static/'


# ☁️ CLOUDINARY CONFIG (IDE ÍRD A SAJÁTOD!)
cloudinary.config(
    cloud_name="A_TE_CLOUD_NAME",
    api_key="A_TE_API_KEY",
    api_secret="A_TE_API_SECRET"
)


# 🔥 KÉPEK CLOUDINARY-BE MENNEK
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# ❗ NE HASZNÁLD EZEKET
# MEDIA_ROOT = ...
# MEDIA_URL = ...


# 🔹 DEFAULT
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'