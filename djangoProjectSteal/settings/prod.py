import os
from .base import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ["localhost", 'rs5kw4rhuuv4fzjs.onion']