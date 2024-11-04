"""
ASGI config for gamenews project.

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gamenews.settings')

application = get_asgi_application()
