# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Django',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    }
}


DEBUG = True

TEMPLATE_DEBUG = True