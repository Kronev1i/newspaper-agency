from .base import *  # noqa
from .base import BASE_DIR
import os

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DEBUG = os.environ.get("DJANGO_DEBUG", "") != "False"

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
