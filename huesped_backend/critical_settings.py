"""
Configuraciones criticas de publicar
"""
__author__ = 'Santi'
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path para los elementos estaticos
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.getenv('SECRET_KEY','SECRET_KEY_HARDCODED')

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DB_NAME = os.getenv('DB_NAME','hce')
DB_USER = os.getenv('DB_USER','postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD','turnos1234')
DB_HOST = os.getenv('DB_HOST','127.0.0.1')
DB_PORT = os.getenv('DB_PORT','32768')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
   }
}

#Configuracion CORS
CORS_ORIGIN_ALLOW_ALL = True

"""
#En produccion
    CORS_ORIGIN_WHITELIST = (
        'hostname.example.com',
    )
"""
