import os

from configurations import Configuration


class Base(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '_3@6ni2p0s&5jt^ujg-yy%lo&w$ttxfhs1w92fwji_0gwe4g4+'

    ALLOWED_HOSTS = []


    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'django.contrib.flatpages',
        'django.contrib.sitemaps',

        'rest_framework',
        'api',

        'users',
        'channels',
        'orders',
        'reviews',
        'banners',

        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.kakao',
        'allauth.socialaccount.providers.naver',

        'robots',
        'axes',
        'pipeline',
        'admin_honeypot',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

        'axes.middleware.AxesMiddleware',
    ]

    ROOT_URLCONF = 'config.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'config', 'templates'),
            ],
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

    WSGI_APPLICATION = 'config.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/2.2/ref/settings/#databases

    # Authentication

    AUTHENTICATION_BACKENDS = (
        'axes.backends.AxesBackend',
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    )

    LOGIN_REDIRECT_URL = '/profile/'
    ACCOUNT_LOGOUT_ON_GET = True


    # Password validation
    # https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/2.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.2/howto/static-files/

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'dist', 'static')

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'config', 'static'),
    ]
    STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
    STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'pipeline.finders.PipelineFinder',
    )


    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    PIPELINE = {
        # 'PIPELINE_ENABLED': True,
        'JS_COMPRESSOR': None,
        'CSS_COMPRESSOR': None,
        'DISABLE_WRAPPER': True,

        'STYLESHEETS': {
            'main': {
                'source_filenames': (
                  'css/style.css',
                ),
                'output_filename': 'css/congtube.css',
            }
        },
        'JAVASCRIPT': {
            'main': {
                'source_filenames': (
                  'js/*.js',
                ),
                'output_filename': 'js/congtube.js',
            }
        },
    }


    # Sites Framework
    # https://docs.djangoproject.com/en/2.2/ref/contrib/sites/#module-django.contrib.sites

    SITE_ID = 1


class Dev(Base):
    DEBUG = True
    INSTALLED_APPS = Base.INSTALLED_APPS + [
        'debug_toolbar',
        'django_extensions',
    ]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(Base.BASE_DIR, 'db.sqlite3'),
        }
    }
    MIDDLEWARE = Base.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    INTERNAL_IPS = [
        '127.0.0.1',
    ]


class Production(Base):
    DEBUG = False

    ALLOWED_HOSTS = Base.ALLOWED_HOSTS + [
        '*'
    ]

    INSTALLED_APPS = Base.INSTALLED_APPS + [
        'storages',
    ]

    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn="https://f9bbc01befeb45258a6a89e1f03e476c@sentry.io/1794364",
        integrations=[DjangoIntegration()]
    )

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': 'congtube-rds.c04yy1qrmeq9.ap-northeast-2.rds.amazonaws.com',
            'PORT': 5432,
            'NAME': 'congtube',
            'USER': 'congtube',
            'PASSWORD': 'congtube',
        }
    }

    AWS_ACCESS_KEY_ID = "AKIA2GB5QVA4PHBPUDHX"
    AWS_SECRET_ACCESS_KEY = "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"

    # Static Setting
    AWS_REGION = 'ap-northeast-2'
    AWS_STORAGE_BUCKET_NAME = 'congtube'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_CLOUDFRONT_DOMAIN = 'static.congtube.com'

    STATICFILES_STORAGE = 'config.storages.S3PipelineManifestStorage'
    STATICFILES_LOCATION = ''
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'

    DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
