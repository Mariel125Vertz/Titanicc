from pathlib import Path
import os

# ----------------------
# Base
# ----------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '123456789'
DEBUG = True

# ----------------------
# Hosts permitidos
# ----------------------
# Lee los hosts permitidos desde la variable de entorno
# Por defecto usa localhost y 127.0.0.1
import os


ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# ----------------------
# Apps instaladas
# ----------------------
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # necesario para DRF
    'django.contrib.messages',  # opcional pero recomendable
    'django.contrib.staticfiles',
    'rest_framework',
    'titanic_app',
]

# ----------------------
# Middleware
# ----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# ----------------------
# URLs y WSGI
# ----------------------
ROOT_URLCONF = 'titanic_project.urls'
WSGI_APPLICATION = 'titanic_project.wsgi.application'

# ----------------------
# Templates
# ----------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'titanic_app' / 'templates'],
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

# ----------------------
# Base de datos
# ----------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------------
# Archivos estáticos
# ----------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'titanic_app' / 'static',
]

# ----------------------
# Opcional: configuración de WhiteNoise para servir static en producción
# ----------------------
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
