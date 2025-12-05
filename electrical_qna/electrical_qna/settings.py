from pathlib import Path
import os
from decouple import config, Config, RepositoryEnv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURE CONFIGURATION: Read custom key.env file
DOTENV_PATH = os.path.join(BASE_DIR, 'key.env')
CONFIG = Config(RepositoryEnv(DOTENV_PATH))

# Securely retrieve the Gemini API Key
GEMINI_API_KEY = CONFIG('GEMINI_API_KEY', default=os.environ.get("GEMINI_API_KEY"))

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-vpf4&_w@^=u*2je&%)!ceas#n(k%zh*bybi+r^_ph8usve#*-d'
DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'emqna'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'electrical_qna.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'electrical_qna.wsgi.application'

# Database: Securely read credentials from key.env
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': CONFIG('DB_NAME', default='qna_db'),
        'USER': CONFIG('DB_USER', default='root'),
        'PASSWORD': CONFIG('DB_PASSWORD', default='rithik200314'),
        'HOST': CONFIG('DB_HOST', default='localhost'),
        'PORT': CONFIG('DB_PORT', default='3306')
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'