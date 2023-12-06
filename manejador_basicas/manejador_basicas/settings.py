import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zdz#(^eef$^&v)5qq80$-2%x(aed6!s*4)&$m%b_8sz=peq%*-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'facturacion',
    'social_django',
    'manejador_basicas'
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

ROOT_URLCONF = 'manejador_basicas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR)],
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

WSGI_APPLICATION = 'manejador_basicas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'facturacion',
        'ENFORCE_SCHEMA': False,  # Puedes ajustar esto según tus necesidades
        'CLIENT': {
            'host': '10.128.0.23',  # Por ejemplo, 'localhost'
            'port': 27017,  # Puerto de tu base de datos MongoDB
            'username': 'userRasi',
            'password': 'rasi2023',
        }
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DB_NAME="mongodb://userRasi:rasi2023@10.128.0.23:27017"

LOGIN_URL = "/login/auth0"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "https://facturacion.us.auth0.com/v2/logout?returnTo=http%3A%2F%2F104.197.213.153:8080"
SOCIAL_AUTH_TRAILING_SLASH = False # Remove end slash from routes
SOCIAL_AUTH_AUTH0_DOMAIN = 'facturacion.us.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = '8wIguEUC21F5tqv66uxFqWLn2fp7Rk9S'
SOCIAL_AUTH_AUTH0_SECRET = 'hggBcQAxygrqE6pB41UpiXorLjMjx8MrUmUAJe0ZMSfnTTFbHtwOcGV9FQtR7TtX'
SOCIAL_AUTH_AUTH0_SCOPE = [
 'openid',
 'profile',
 'email',
 'role',
]
AUTHENTICATION_BACKENDS = {
 'manejador_basicas.auth0backend.Auth0',
 'django.contrib.auth.backends.ModelBackend',
}


SESSION_COOKIE_SAMESITE = None

CSRF_TRUSTED_ORIGINS = ['http://34.41.112.180:8000',
                        'http://34.27.72.24:8080',
                        'http://34.135.70.6:8080/'] 


