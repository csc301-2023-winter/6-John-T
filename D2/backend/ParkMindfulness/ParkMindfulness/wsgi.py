"""
WSGI config for ParkMindfulness project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

# ANYONE WHO CHANGES THIS FILE THAT IS NOT TAJWAAR GETS PUT INTO ZOOM CALL WITH JOKER MICHELE

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ParkMindfulness.settings")

application = get_wsgi_application()
